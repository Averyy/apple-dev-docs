# Creating 3D objects from photographs

**Framework**: RealityKit

Construct virtual objects to use in your AR experiences.

#### Overview

In iOS 17 and later, and macOS 12 and later, to create a 3D object from a series of photographs, submit the images to RealityKit using a [`PhotogrammetrySession`](photogrammetrysession.md), register to receive status updates, and start the session. The completed process produces a 3D representation of the photographed object that you can use in your app or export to other software like .

For more information on capturing high-quality images for photogrammetry, see [`Capturing photographs for RealityKit Object Capture`](capturing-photographs-for-realitykit-object-capture.md).

##### Check for Availability

RealityKit Object Capture is only available on Mac computers that meet the minimum requirements for performing object reconstruction, including a GPU with at least 4 GB of RAM and ray tracing support. It is also available on select iOS devices with LiDAR capabilities.

Before using any Object Capture APIs, check whether the device your code is running on meets those requirements, and only proceed if it does.

```swift
guard PhotogrammetrySession.isSupported else {
    // Inform user and don't proceed with reconstruction.
}
```

##### Create the Photogrammetry Session

Begin by creating a [`PhotogrammetrySession.Request`](photogrammetrysession/request.md) with a URL that points to the desired output location for the generated USDZ file and the desired level of detail for the model. Next, use that request, along with a URL pointing to the directory containing your images, to create the [`PhotogrammetrySession`](photogrammetrysession.md) object.

```swift
let inputFolderUrl = URL(fileURLWithPath: "/tmp/MyInputImages/")
let url = URL(fileURLWithPath: "MyObject.usdz")
var request = PhotogrammetrySession.Request.modelFile(url: url, 
                                                      detail: .full)
guard let session = try PhotogrammetrySession(input: inputFolderUrl) else {
    return 
} 
```

##### Listen for Updates and Begin Creation

RealityKit uses an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) of [`PhotogrammetrySession.Output`](photogrammetrysession/output.md) objects to deliver status updates about the object-creation process in the background. To update your app’s UI or to take other actions as a result of these status updates, create an `async` task and use a `for`-`try`-`await` loop on [`outputs`](photogrammetrysession/outputs-swift.property.md).

```swift
let waiter = async {
    do {
        for try await output in session.outputs {
            switch output {
                case .processingComplete:
                    // RealityKit has processed all requests.
                case .requestError(let request, let error):
                    // Request encountered an error.
                case .requestComplete(let request, let result):
                    // RealityKit has finished processing a request.
                case .requestProgress(let request, let fractionComplete):
                    // Periodic progress update. Update UI here.
                case .inputComplete: 
                    // Ingestion of images is complete and processing begins.
                case .invalidSample(let id, let reason):
                    // RealityKit deemed a sample invalid and didn't use it.
                case .skippedSample(let id):
                    // RealityKit was unable to use a provided sample.
                case .automaticDownsampling:
                    // RealityKit downsampled the input images because of
                    // resource constraints.
                case .processingCancelled
                    // Processing was canceled.
                @unknown default:
                    // Unrecognized output.
            }
        }
    } catch {
        print("Output: ERROR = \(String(describing: error))")
        // Handle error.
    }
}
```

Once you’ve created a session and registered to receive status updates, start the object-creation process by calling [`process(requests:)`](photogrammetrysession/process(requests:).md). RealityKit processes the photographs in the background and notifies your app when the process completes or fails.

```swift
session.process(requests: [request])
```

##### Compensate for Challenging Images

RealityKit’s default photogrammetry settings work for the vast majority of input images. If, however, you have image sets that are low contrast or lack many identifying landmarks, you can override the default values to compensate by creating a [`PhotogrammetrySession.Configuration`](photogrammetrysession/configuration-swift.struct.md) object and passing it into the initializer when you create your [`PhotogrammetrySession`](photogrammetrysession.md).

To simplify the object-creation process, you can use a custom configuration to provide images to the [`PhotogrammetrySession`](photogrammetrysession.md) in sequence by listing adjacent images together, or to control support for object masking, which blocks out portions of an image around an object.

```swift
let config = Configuration()

// Use slower, more sensitive landmark detection.
config.featureSensitivity = .high
// Adjacent images are next to each other.
config.sampleOrdering = .sequential
// Object masking is enabled.
config.isObjectMaskingEnabled = true

let session = try PhotogrammetrySession(input: inputFolderUrl, 
                                        configuration:config)
```

## See Also

- [Capturing photographs for RealityKit Object Capture](capturing-photographs-for-realitykit-object-capture.md)
  Take high-quality images of objects to generate 3D models.
- [Scanning objects using Object Capture](scanning-objects-using-object-capture.md)
  Implement a full scanning workflow for capturing objects on iOS devices.
- [Building an object reconstruction app](building-an-object-reconstruction-app.md)
  Reconstruct objects from user-selected input images by using photogrammetry.
- [Creating a photogrammetry command-line app](creating-a-photogrammetry-command-line-app.md)
  Generate 3D objects from images using RealityKit Object Capture.
- [Using object capture assets in RealityKit](using-object-capture-assets-in-realitykit.md)
  Create a chess game using RealityKit and assets created using Object Capture.
- [class PhotogrammetrySession](photogrammetrysession.md)
  Manages the creation of a 3D model from a set of images.
- [struct PhotogrammetrySample](photogrammetrysample.md)
  An object that represents one image and its corresponding metadata.
- [struct ObjectCaptureView](objectcaptureview.md)
  A view that guides a user through capturing images for object capture.
- [class ObjectCaptureSession](objectcapturesession.md)
  A session object that monitors and controls image capture for photogrammetry.
- [struct ObjectCapturePointCloudView](objectcapturepointcloudview.md)
  Renders the current state of the point cloud from an object capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/creating-3d-objects-from-photographs)*