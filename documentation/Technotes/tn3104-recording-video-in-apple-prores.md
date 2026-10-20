# TN3104: Recording video in Apple ProRes

**Framework**: Technotes  
**Role**: Technote

Configure pieces of an AVCaptureSession to capture video in Apple ProRes.

#### Overview

iPhone 13 Pro supports Apple ProRes video recording up to 4k at 30 fps and 1080p at 60 fps (except the 128GB model, which supports Apple ProRes video recording up to 1080p at 30 fps). This Technote details how to configure an AVCapture pipeline to capture and record a video encoded in Apple ProRes 422.

For a general overview of Apple ProRes codecs, see [About Apple ProRes](https://support.apple.com/en-us/HT202410).

#### Choosing a preset

Capturing video in Apple ProRes requires manual configuration of the [`AVCaptureDevice`](../AVFoundation/avcapturedevice.md)’s [`activeFormat`](../AVFoundation/avcapturedevice/activeformat.md). There is no [`AVCaptureSession.Preset`](../AVFoundation/avcapturesession/preset.md) available that supports capture in Apple ProRes. For this reason, set the [`sessionPreset`](../AVFoundation/avcapturesession/sessionpreset.md) of your [`AVCaptureSession`](../AVFoundation/avcapturesession.md) to [`inputPriority`](../AVFoundation/avcapturesession/preset/inputpriority.md), which specifies that the [`AVCaptureSession`](../AVFoundation/avcapturesession.md) should not automatically configure its inputs and outputs.

#### Selecting a capture format

As described in [About Apple ProRes](https://support.apple.com/en-us/HT202410), Apple ProRes 422 codecs require 10-bits-per-channel video sources, and Apple ProRes 4444 codecs support up to 12-bits-per-channel and up to 16 bits for the alpha channel. If you iterated through all of the supported capture [`formats`](../AVFoundation/avcapturedevice/formats.md) of an [`AVCaptureDevice`](../AVFoundation/avcapturedevice.md) on iPhone 13 Pro, you would see capture formats with one of the following pixel formats:

| Pixel Format Constant | FourCharCode | Bits Per Channel |
| --- | --- | --- |
| kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange | ‘420v’ | 8 |
| kCVPixelFormatType_420YpCbCr8BiPlanarFullRange | ‘420f’ | 8 |
| kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange | ‘x420’ | 10 |
| kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange | ‘x422’ | 10 |

Notice that there are no supported capture formats that capture at higher than 10-bits-per-channel, also notice that none of the supported capture formats use a 4:4:4 pixel format. Therefore, none of the capture formats output video data that is suitable as a video source for Apple ProRes 4444 codecs.

To find a capture format that is suitable as a video source for an Apple ProRes 422 codec, you should iterate through the capture [`formats`](../AVFoundation/avcapturedevice/formats.md) of the [`AVCaptureDevice`](../AVFoundation/avcapturedevice.md), and return a capture format whose [`mediaSubType`](../CoreMedia/cmformatdescription/mediasubtype-swift.property.md) is [`kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange`](../CoreVideo/kcvpixelformattype_422ypcbcr10biplanarvideorange.md):

```swift
extension AVCaptureDevice {
    func findFormat() -> AVCaptureDevice.Format? {
        // Iterate over the supported capture formats.
        for captureFormat in formats {
            // Check if the captureFormat's pixel format is equivalent to the target pixel format.
            if captureFormat.formatDescription.mediaSubType.rawValue == kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange {
                // Check if other criteria is met.  For example, you may want to target a particular resolution or max frame rate.
                if otherCriteriaIsMet {
                    // Once all criteria is met, return the current format.
                    return format
                }
            }
        }
        // If there is no supported capture format that meets the selection criteria, return nil. Your app may wish to fallback to some other capture format in this case.
        return nil
    }
}
```

Once you have identified a capture format suitable for Apple ProRes 422, set it as the [`activeFormat`](../AVFoundation/avcapturedevice/activeformat.md) of your capture device, and ensure that the capture device has a corresponding [`AVCaptureDeviceInput`](../AVFoundation/avcapturedeviceinput.md) which you have successfully added as an input to the [`AVCaptureSession`](../AVFoundation/avcapturesession.md). See [Setting up a capture session](../AVFoundation/setting-up-a-capture-session.md) for more information about adding inputs to a capture session.

#### Choosing an output type

For many apps, using an [`AVCaptureMovieFileOutput`](../AVFoundation/avcapturemoviefileoutput.md) to write an Apple ProRes movie file is sufficient.

If you require a greater amount of control when writing the movie file, or you need access to video samples before they are written to a movie file, then you can use an [`AVCaptureVideoDataOutput`](../AVFoundation/avcapturevideodataoutput.md) to get access to the video samples. Next, you can process or inspect the video samples, and then submit the video samples to an [`AVAssetWriter`](../AVFoundation/avassetwriter.md).

#### Configuring the output

[`AVCaptureMovieFileOutput`](../AVFoundation/avcapturemoviefileoutput.md) supports writing movie files encoded with Apple ProRes 422 codecs. To check the available video codecs at runtime, you can iterate through the [`availableVideoCodecTypes`](../AVFoundation/avcapturemoviefileoutput/availablevideocodectypes.md).

The [`availableVideoCodecTypes`](../AVFoundation/avcapturemoviefileoutput/availablevideocodectypes.md) array is dynamic, and depends on the [`activeFormat`](../AVFoundation/avcapturedevice/activeformat.md) of the [`AVCaptureDeviceInput`](../AVFoundation/avcapturedeviceinput.md) that is connected to the same [`AVCaptureSession`](../AVFoundation/avcapturesession.md) as the [`AVCaptureMovieFileOutput`](../AVFoundation/avcapturemoviefileoutput.md). For this reason, you should check for support of Apple ProRes 422 codecs only after you have configured the capture device to capture in an ‘x422’ format.

Once you have verified that the movie file output supports your desired Apple ProRes 422 codec, use the [`outputSettings(for:)`](../AVFoundation/avcapturemoviefileoutput/outputsettings%28for%29.md) method to set specify the codec that the output should use:

```swift
// Ensure that the availableVideoCodecTypes contains the target codec.
guard movieFileOutput.availableVideoCodecTypes.contains(where: {
    $0 == .proRes422
}) else { fatalError("Target codec is not supported in the current configuration.") }

guard let videoConnection = movieFileOutput.connection(with: .video) else {
    fatalError("The movie file output is not connected to a video input.")
}

// Set the output settings of the movieFileOutput.
movieFileOutput.setOutputSettings([AVVideoCodecKey : AVVideoCodecType.proRes422.rawValue], for: videoConnection)
```

[`AVCaptureVideoDataOutput`](../AVFoundation/avcapturevideodataoutput.md) does not require any special configuration to be compatible with an ‘x422’ input, simply set its sample buffer delegate with the [`setSampleBufferDelegate(_:queue:)`](../AVFoundation/avcapturevideodataoutput/setsamplebufferdelegate%28_,queue%29.md) method, and add the output to the capture session.

#### Recording and saving with AVCaptureMovieFileOutput

Use the [`startRecording(to:recordingDelegate:)`](../AVFoundation/avcapturefileoutput/startrecording%28to,recordingdelegate%29.md) method to set a recording delegate and start recording to a file. When recording is stopped, you will receive the output file in [`fileOutput(_:didFinishRecordingTo:from:error:)`](../AVFoundation/avcapturefileoutputrecordingdelegate/fileoutput%28_,didfinishrecordingto,from,error%29.md). You can save this movie file directly to the Photo Library using the [`creationRequestForAssetFromVideo(atFileURL:)`](https://developer.apple.com/documentation/photos/phassetchangerequest/creationrequestforassetfromvideo(atfileurl:)) method. Once saved, you can view the video in the Photos app, where you will notice that the asset has a “ProRes” badge in the upper-left corner.

#### Recording and saving with AVCaptureVideoDataOutput and AVAssetWriter

Once you have decided to start recording, create an [`AVAssetWriter`](../AVFoundation/avassetwriter.md), and an [`AVAssetWriterInput`](../AVFoundation/avassetwriterinput.md). When you create the [`AVAssetWriterInput`](../AVFoundation/avassetwriterinput.md), specify outputSettings that use your preferred Apple ProRes 422 video codec. You can request recommended settings from the [`AVCaptureVideoDataOutput`](../AVFoundation/avcapturevideodataoutput.md):

```swift
let fileType = AVFileType.mov

// Request the recommended video settings for your target codec.
let outputSettings = videoDataOutput.recommendedVideoSettings(forVideoCodecType: .proRes422, assetWriterOutputFileType: fileType)

// Use the video settings to initialize your video input for writing.
writerVideoInput = AVAssetWriterInput(mediaType: .video, outputSettings: outputSettings)

// Specify that you have a real-time video sample source.
writerVideoInput.expectsMediaDataInRealTime = true

// Create the AVAssetWriter using your outputURL.
do {
    assetWriter = try AVAssetWriter(outputURL: outputURL, fileType: fileType)
} catch {
    // Handle errors here.
}

// Add the video input to the asset writer.
assetWriter.add(writerVideoInput)
```

Take the video samples that you receive in the [`captureOutput(_:didOutput:from:)`](../AVFoundation/avcapturevideodataoutputsamplebufferdelegate/captureoutput%28_,didoutput,from%29.md) delegate method and append them to your movie file [`AVAssetWriterInput`](../AVFoundation/avassetwriterinput.md):

```swift
// Start the asset writer if it hasn't been started already, and use the first sampleBuffer's presentationTimeStamp as the source time.
if assetWriter.status != .writing {
    assetWriter.startWriting()
    assetWriter.startSession(atSourceTime: sampleBuffer.presentationTimeStamp)
}

// Append the sample buffer if the video input is ready.
if writerVideoInput.isReadyForMoreMediaData {
    writerVideoInput.append(sampleBuffer)
}
```

When you decide to stop recording, call [`finishWriting(completionHandler:)`](../AVFoundation/avassetwriter/finishwriting%28completionhandler%29.md). In the completion handler, you can save the movie file directly to the Photo Library using the [`creationRequestForAssetFromVideo(atFileURL:)`](https://developer.apple.com/documentation/photos/phassetchangerequest/creationrequestforassetfromvideo(atfileurl:)) method, passing in the [`outputURL`](../AVFoundation/avassetwriter/outputurl.md) of the asset writer. Once saved, you can view the video in the Photos app, where you will notice that the asset has a “ProRes” badge in the upper-left corner.

#### Revision History

- **2022-05-24** Made minor editorial changes.
- **2022-02-08** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3104-recording-video-in-apple-prores)*