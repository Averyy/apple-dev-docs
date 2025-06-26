# TN3104: Recording video in Apple ProRes

**Framework**: Technotes

Configure pieces of an AVCaptureSession to capture video in Apple ProRes.

#### Overview

iPhone 13 Pro supports Apple ProRes video recording up to 4k at 30 fps and 1080p at 60 fps (except the 128GB model, which supports Apple ProRes video recording up to 1080p at 30 fps). This Technote details how to configure an AVCapture pipeline to capture and record a video encoded in Apple ProRes 422.

For a general overview of Apple ProRes codecs, see [`About Apple ProRes`](https://developer.apple.comhttps://support.apple.com/en-us/HT202410).

#### Choosing a Preset

Capturing video in Apple ProRes requires manual configuration of the [`AVCaptureDevice`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice)’s [`activeFormat`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/activeFormat). There is no [`AVCaptureSession.Preset`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/Preset) available that supports capture in Apple ProRes. For this reason, set the [`sessionPreset`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/sessionPreset) of your [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) to [`inputPriority`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession/Preset/inputPriority), which specifies that the [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) should not automatically configure its inputs and outputs.

#### Selecting a Capture Format

As described in [`About Apple ProRes`](https://developer.apple.comhttps://support.apple.com/en-us/HT202410), Apple ProRes 422 codecs require 10-bits-per-channel video sources, and Apple ProRes 4444 codecs support up to 12-bits-per-channel and up to 16 bits for the alpha channel. If you iterated through all of the supported capture [`formats`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/formats) of an [`AVCaptureDevice`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice) on iPhone 13 Pro, you would see capture formats with one of the following pixel formats:

| Pixel Format Constant | FourCharCode | Bits Per Channel |
| --- | --- | --- |
| kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange | ‘420v’ | 8 |
| kCVPixelFormatType_420YpCbCr8BiPlanarFullRange | ‘420f’ | 8 |
| kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange | ‘x420’ | 10 |
| kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange | ‘x422’ | 10 |

Notice that there are no supported capture formats that capture at higher than 10-bits-per-channel, also notice that none of the supported capture formats use a 4:4:4 pixel format. Therefore, none of the capture formats output video data that is suitable as a video source for Apple ProRes 4444 codecs.

To find a capture format that is suitable as a video source for an Apple ProRes 422 codec, you should iterate through the capture [`formats`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/formats) of the [`AVCaptureDevice`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice), and return a capture format whose [`mediaSubType`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescription/mediaSubType-swift.property) is [`kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange):

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

Once you have identified a capture format suitable for Apple ProRes 422, set it as the [`activeFormat`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/activeFormat) of your capture device, and ensure that the capture device has a corresponding [`AVCaptureDeviceInput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDeviceInput) which you have successfully added as an input to the [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession). See [`Setting Up a Capture Session`](https://developer.apple.com/documentation/AVFoundation/setting-up-a-capture-session) for more information about adding inputs to a capture session.

#### Choosing an Output Type

For many apps, using an [`AVCaptureMovieFileOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureMovieFileOutput) to write an Apple ProRes movie file is sufficient.

If you require a greater amount of control when writing the movie file, or you need access to video samples before they are written to a movie file, then you can use an [`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput) to get access to the video samples. Next, you can process or inspect the video samples, and then submit the video samples to an [`AVAssetWriter`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriter).

#### Configuring the Output

[`AVCaptureMovieFileOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureMovieFileOutput) supports writing movie files encoded with Apple ProRes 422 codecs. To check the available video codecs at runtime, you can iterate through the [`availableVideoCodecTypes`](https://developer.apple.com/documentation/AVFoundation/AVCaptureMovieFileOutput/availableVideoCodecTypes).

The [`availableVideoCodecTypes`](https://developer.apple.com/documentation/AVFoundation/AVCaptureMovieFileOutput/availableVideoCodecTypes) array is dynamic, and depends on the [`activeFormat`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/activeFormat) of the [`AVCaptureDeviceInput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDeviceInput) that is connected to the same [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) as the [`AVCaptureMovieFileOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureMovieFileOutput). For this reason, you should check for support of Apple ProRes 422 codecs only after you have configured the capture device to capture in an ‘x422’ format.

Once you have verified that the movie file output supports your desired Apple ProRes 422 codec, use the [`outputSettings(for:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureMovieFileOutput/outputSettings(for:)) method to set specify the codec that the output should use:

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

[`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput) does not require any special configuration to be compatible with an ‘x422’ input, simply set its sample buffer delegate with the [`setSampleBufferDelegate(_:queue:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput/setSampleBufferDelegate(_:queue:)) method, and add the output to the capture session.

#### Recording and Saving with Avcapturemoviefileoutput

Use the [`startRecording(to:recordingDelegate:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureFileOutput/startRecording(to:recordingDelegate:)) method to set a recording delegate and start recording to a file. When recording is stopped, you will receive the output file in [`fileOutput(_:didFinishRecordingTo:from:error:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureFileOutputRecordingDelegate/fileOutput(_:didFinishRecordingTo:from:error:)). You can save this movie file directly to the Photo Library using the [`creationRequestForAssetFromVideo(atFileURL:)`](https://developer.apple.com/documentation/Photos/PHAssetChangeRequest/creationRequestForAssetFromVideo(atFileURL:)) method. Once saved, you can view the video in the Photos app, where you will notice that the asset has a “ProRes” badge in the upper-left corner.

#### Recording and Saving with Avcapturevideodataouput and Avassetwriter

Once you have decided to start recording, create an [`AVAssetWriter`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriter), and an [`AVAssetWriterInput`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriterInput). When you create the [`AVAssetWriterInput`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriterInput), specify outputSettings that use your preferred Apple ProRes 422 video codec. You can request recommended settings from the [`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput):

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

Take the video samples that you receive in the [`captureOutput(_:didOutput:from:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutputSampleBufferDelegate/captureOutput(_:didOutput:from:)) delegate method and append them to your movie file [`AVAssetWriterInput`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriterInput):

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

When you decide to stop recording, call [`finishWriting(completionHandler:)`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriter/finishWriting(completionHandler:)). In the completion handler, you can save the movie file directly to the Photo Library using the [`creationRequestForAssetFromVideo(atFileURL:)`](https://developer.apple.com/documentation/Photos/PHAssetChangeRequest/creationRequestForAssetFromVideo(atFileURL:)) method, passing in the [`outputURL`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriter/outputURL) of the asset writer. Once saved, you can view the video in the Photos app, where you will notice that the asset has a “ProRes” badge in the upper-left corner.

#### Revision History

-  Made minor editorial changes.
-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3104-recording-video-in-apple-prores)*