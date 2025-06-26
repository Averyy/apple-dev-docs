# Capturing Photos in RAW and Apple ProRAW Formats

**Framework**: AVFoundation

Support professional photography workflows by enabling minimally processed image capture in your camera app.

#### Overview

By default, the image-capture pipeline uses advanced computational photography techniques to achieve the highest quality images, and delivers the processed result to your app in a compressed format for efficient storage and display. Processed formats are a great choice in many cases, but RAW formats contain minimally processed image data from the camera sensor, which gives your app users more creative control.

Capturing images in RAW formats results in much larger files than compressed formats, but greatly expands editing capabilities in post-production. One drawback to shooting in standard RAW formats is that it bypasses the advanced processing that the image-capture pipeline provides.

Beginning in iOS 14.3, and available on iPhone 12 Pro and Pro Max, you can use the Apple ProRAW format. The Apple ProRAW format provides the benefits of RAW capture, and applies many of the multi-image fusion techniques previously unavailable to RAW workflows.

> 💡 **Tip**:  You can use Core Image to display and edit RAW and Apple ProRAW files. See the [`CIRAWFilter`](https://developer.apple.com/documentation/CoreImage/CIRAWFilter) class’s [`init(imageURL:)`](https://developer.apple.com/documentation/CoreImage/CIRAWFilter/init(imageURL:)) initializer for more information.

##### Enable Apple Proraw Support

To determine whether your app’s photo output supports the Apple ProRAW format in the current environment, add the output to a capture session that has a connected video source, and query its [`isAppleProRAWSupported`](avcapturephotooutput/isappleprorawsupported.md) property. If the current environment supports the Apple ProRAW format, you can enable the photo output to use it by setting its [`isAppleProRAWEnabled`](avcapturephotooutput/isappleprorawenabled.md) property to [`true`](https://developer.apple.com/documentation/swift/true) as the example below shows:

```swift
private let captureSession = AVCaptureSession()
private let photoOutput = AVCapturePhotoOutput()

private func setupSession() throws {
    
    // Start the capture session configuration.
    captureSession.beginConfiguration()
    
    // Configure the session for photo capture.
    captureSession.sessionPreset = .photo
    
    // Connect the default video device.
    let videoInput = try AVCaptureDeviceInput(device: defaultVideoDevice)
    if captureSession.canAddInput(videoInput) {
        captureSession.addInput(videoInput)
        currentVideoInput = videoInput
    } else {
        throw CameraError.setupFailed
    }
    
    // Connect and configure the capture output.
    if captureSession.canAddOutput(photoOutput) {
        captureSession.addOutput(photoOutput)
        
        // Use the Apple ProRAW format when the environment supports it.
        photoOutput.isAppleProRAWEnabled = photoOutput.isAppleProRAWSupported
    } else {
        throw CameraError.setupFailed
    }
    
    // Session configuration is complete. Commit the configuration.
    captureSession.commitConfiguration()
}

```

Enabling use of the Apple ProRAW format adds an entry to the photo output’s [`availableRawPhotoPixelFormatTypes`](avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) array. You can determine whether a particular format in the array is an Apple ProRAW or a Bayer RAW format by querying the output’s [`isAppleProRAWPixelFormat(_:)`](avcapturephotooutput/isappleprorawpixelformat(_:).md) or [`isBayerRAWPixelFormat(_:)`](avcapturephotooutput/isbayerrawpixelformat(_:).md) methods.

> ❗ **Important**:  To avoid a lengthy reconfiguration of the capture pipeline, enable Apple ProRAW capture before starting the capture session.

##### Capture Raw and Apple Proraw Photos

Capturing photos in RAW and Apple ProRAW formats requires only minor changes to the basic photography workflow in [`Capturing Still and Live Photos`](capturing-still-and-live-photos.md). Begin by creating an [`AVCapturePhotoSettings`](avcapturephotosettings.md) object that specifies the RAW format to capture, and optionally, a processed format to capture if your app supports creating RAW+JPEG files. The capture pipeline only supports the RAW formats in the photo output’s [`availableRawPhotoPixelFormatTypes`](avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) array.

The example below finds the appropriate RAW format, choosing the Apple ProRAW format when it’s in an enabled state, and the Bayer RAW format when it’s not. It creates a photo settings object that specifies the RAW and processed formats, and a delegate object to monitor the capture progress. Finally, it calls the photo output’s [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, passing it the photo settings and delegate objects.

```swift
let query = photoOutput.isAppleProRAWEnabled ?
    { AVCapturePhotoOutput.isAppleProRAWPixelFormat($0) } :
    { AVCapturePhotoOutput.isBayerRAWPixelFormat($0) }

// Retrieve the RAW format, favoring the Apple ProRAW format when it's in an enabled state.
guard let rawFormat =
        photoOutput.availableRawPhotoPixelFormatTypes.first(where: query) else {
    fatalError("No RAW format found.")
}

// Capture a RAW format photo, along with a processed format photo.
let processedFormat = [AVVideoCodecKey: AVVideoCodecType.hevc]
let photoSettings = AVCapturePhotoSettings(rawPixelFormatType: rawFormat,
                                           processedFormat: processedFormat)

// Create a delegate to monitor the capture process.
let delegate = RAWCaptureDelegate()
captureDelegates[photoSettings.uniqueID] = delegate

// Remove the delegate reference when it finishes its processing.
delegate.didFinish = {
    self.captureDelegates[photoSettings.uniqueID] = nil
}

// Tell the output to capture the photo.
photoOutput.capturePhoto(with: photoSettings, delegate: delegate)
```

The Apple ProRAW format supports capturing up to a full-resolution JPEG image to use as a thumbnail photo. Set [`rawEmbeddedThumbnailPhotoFormat`](avcapturephotosettings/rawembeddedthumbnailphotoformat.md) on your photo settings object as the following example shows:

```swift
// Select the first available codec type, which is JPEG.
guard let thumbnailPhotoCodecType =
    photoSettings.availableRawEmbeddedThumbnailPhotoCodecTypes.first else {
    // Handle the failure to find an available thumbnail photo codec type.
}

// Select the maximum photo dimensions as thumbnail dimensions if a full-size thumbnail is desired.
// The system clamps these dimensions to the photo dimensions if the capture produces a photo with smaller than maximum dimensions.
let dimensions = photoSettings.maxPhotoDimensions

photoSettings.rawEmbeddedThumbnailPhotoFormat = [
    AVVideoCodecKey: thumbnailPhotoCodecType,
    AVVideoWidthKey: dimensions.width,
    AVVideoHeightKey: dimensions.height
]
```

##### Handle the Captured Photos

The photo output calls its delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method at least once for each format you request, and possibly additional times, depending on your capture settings. Using the capture settings in the previous section results in the photo output calling this delegate method twice: once for the RAW or Apple ProRAW image, and again for the processed image. In each invocation, get the photo’s file data by calling its [`fileDataRepresentation()`](avcapturephoto/filedatarepresentation().md) method and store it as necessary. If you call this method on a RAW or Apple ProRAW photo, it returns the data in the industry-standard DNG file format. If you call it on processed images, it returns the compressed bitmap image data.

The following code shows an example implementation of the [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method. It writes the RAW file to disk and stores a reference to the processed photo’s compressed bitmap data for later use.

```swift
class RAWCaptureDelegate: NSObject, AVCapturePhotoCaptureDelegate {
    
    private var rawFileURL: URL?
    private var compressedData: Data?
    
    var didFinish: (() -> Void)?
    
    // Store the RAW file and compressed photo data until the capture finishes.
    func photoOutput(_ output: AVCapturePhotoOutput,
                     didFinishProcessingPhoto photo: AVCapturePhoto,
                     error: Error?) {
        
        guard error == nil else {
            print("Error capturing photo: \(error!)")
            return
        }
        
        // Access the file data representation of this photo.
        guard let photoData = photo.fileDataRepresentation() else {
            print("No photo data to write.")
            return
        }
        
        if photo.isRawPhoto {
            // Generate a unique URL to write the RAW file.
            rawFileURL = makeUniqueDNGFileURL()
            do {
                // Write the RAW (DNG) file data to a URL.
                try photoData.write(to: rawFileURL!)
            } catch {
                fatalError("Couldn't write DNG file to the URL.")
            }
        } else {
            // Store compressed bitmap data.
            compressedData = photoData
        }
    }
    
    private func makeUniqueDNGFileURL() -> URL {
        let tempDir = FileManager.default.temporaryDirectory
        let fileName = ProcessInfo.processInfo.globallyUniqueString
        return tempDir.appendingPathComponent(fileName).appendingPathExtension("dng")
    }
}
```

##### Customize the Apple Proraw Output

By default, when you ask for the file data representation of an Apple ProRAW photo, you get the data in full lossless quality. If you’re willing to accept some lossy compression to achieve smaller file sizes, you can customize the compression settings by calling [`fileDataRepresentation(with:)`](avcapturephoto/filedatarepresentation(with:).md) and passing it a custom object that conforms to the [`AVCapturePhotoFileDataRepresentationCustomizer`](avcapturephotofiledatarepresentationcustomizer.md) protocol. The following code shows an example implementation of this protocol that applies minimal compression to the output image:

```swift
class AppleProRAWCustomizer: NSObject, AVCapturePhotoFileDataRepresentationCustomizer {
    
    // Customize the compression settings.
    func replacementAppleProRAWCompressionSettings(for photo: AVCapturePhoto, 
                                                   defaultSettings: [String : Any], 
                                                   maximumBitDepth: Int) -> [String : Any] {
        
        // Reduce the bit depth and quality of the final file.
        return [AVVideoAppleProRAWBitDepthKey: maximumBitDepth - 2, 
                AVVideoQualityKey: 0.95]
    }
}
```

To use this customizer when retrieving the file data representation of a ProRAW photo, create a new instance of your customizer and pass it to the [`fileDataRepresentation(with:)`](avcapturephoto/filedatarepresentation(with:).md) method as the example below shows:

```swift
// Get a minimally compressed representation of the file data.
let customizer = AppleProRAWCustomizer()
let photoData = photo.fileDataRepresentation(with: customizer)
```

##### Save the Photos to the Photos Library

The photo output indicates when it finishes the capture request by calling the delegate’s [`photoOutput(_:didFinishCaptureFor:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:).md) method. This callback provides an opportunity to save the captured photos to the user’s Photos library. For more information about configuring your app to access the user’s Photos library, see [`Saving Captured Photos`](saving-captured-photos.md).

To save the captured photos to the user’s Photos library, create a single Photos asset that associates the RAW or Apple ProRAW data with the processed data. Create an instance of [`PHAssetCreationRequest`](https://developer.apple.com/documentation/Photos/PHAssetCreationRequest), then specify the DNG version as the asset’s main [`PHAssetResourceType.photo`](https://developer.apple.com/documentation/Photos/PHAssetResourceType/photo) resource, and the processed image as an [`PHAssetResourceType.alternatePhoto`](https://developer.apple.com/documentation/Photos/PHAssetResourceType/alternatePhoto) resource. Perform the request inside a change block as the example below shows:

```swift
// After both RAW and compressed versions are complete, add them to the Photos library.
func photoOutput(_ output: AVCapturePhotoOutput,
                 didFinishCaptureFor resolvedSettings: AVCaptureResolvedPhotoSettings,
                 error: Error?) {
    
    // Call the "finished" closure, if you set it.
    defer { didFinish?() }
    
    guard error == nil else {
        print("Error capturing photo: \(error!)")
        return
    }
    
    // Ensure the RAW and processed photo data exists.
    guard let rawFileURL = rawFileURL,
          let compressedData = compressedData else {
        print("The expected photo data isn't available.")
        return
    }
    
    // Request add-only access to the user's Photos library (if the user hasn't already granted that access).
    PHPhotoLibrary.requestAuthorization(for: .addOnly) { status in
        
        // Don't continue unless the user granted access.
        guard status == .authorized else { return }
        
        PHPhotoLibrary.shared().performChanges {
            
            let creationRequest = PHAssetCreationRequest.forAsset()
            
            // Save the RAW (DNG) file as the main resource for the Photos asset.
            let options = PHAssetResourceCreationOptions()
            options.shouldMoveFile = true
            creationRequest.addResource(with: .photo,
                                        fileURL: rawFileURL,
                                        options: options)
            
            
            // Add the compressed (HEIF) data as an alternative resource.
            creationRequest.addResource(with: .alternatePhoto,
                                        data: compressedData,
                                        options: nil)
            
        } completionHandler: { success, error in
            // Process the Photos library error.
        }
    }
}
```

## See Also

- [Capturing consistent color images](capturing-consistent-color-images.md)
  Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing Still and Live Photos](capturing-still-and-live-photos.md)
  Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Supporting Continuity Camera in Your Mac App](../AppKit/supporting-continuity-camera-in-your-mac-app.md)
  Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [class AVCapturePhoto](avcapturephoto.md)
  A container for image data from a photo capture output.
- [class AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md)
  A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [class AVCapturePhotoOutput](avcapturephotooutput.md)
  A capture output for still image, Live Photos, and other photography workflows.
- [protocol AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md)
  Methods for monitoring progress and receiving results from a photo capture output.
- [class AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md)
  An object that monitors changes to a photo output’s capture readiness.
- [protocol AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md)
  A delegate protocol to receive updates about a photo output’s capture readiness.
- [class AVCaptureStillImageOutput](avcapturestillimageoutput.md)
  A capture output for capturing still photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/capturing-photos-in-raw-and-apple-proraw-formats)*