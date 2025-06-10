# PhotogrammetrySession.Output

**Framework**: RealityKit  
**Kind**: enum

Status updates on the object-creation process.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Output
```

## Mentions

- [Creating 3D objects from photographs](creating-3d-objects-from-photographs.md)

#### Overview

RealityKit’s Object Capture is a long-running background task. The session publishes messages status and error messages to [`outputs`](photogrammetrysession/outputs-swift.property.md), a Swift [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence).

Your app can respond to these updates using a `for`-`await`-`in` loop inside of a `Task`, as this example demonstrates.

```swift
let waiter = Task {
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
                case requestProgressInfo(let request, let progressInfo):
                    // Periodic progress info update.
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

## Topics

### Monitoring session status
- [PhotogrammetrySession.Output.inputComplete](photogrammetrysession/output/inputcomplete.md)
  The data ingestion portion of the process is complete.
- [PhotogrammetrySession.Output.processingComplete](photogrammetrysession/output/processingcomplete.md)
  The session completed a request successfully.
- [PhotogrammetrySession.Output.processingCancelled](photogrammetrysession/output/processingcancelled.md)
  All pending requests are canceled.
### Monitoring request status
- [case requestProgress(PhotogrammetrySession.Request, fractionComplete: Double)](photogrammetrysession/output/requestprogress(_:fractioncomplete:).md)
  A progress update provided by the session.
- [case requestComplete(PhotogrammetrySession.Request, PhotogrammetrySession.Result)](photogrammetrysession/output/requestcomplete(_:_:).md)
  The session finished handling all pending requests.
- [case requestError(PhotogrammetrySession.Request, any Error)](photogrammetrysession/output/requesterror(_:_:).md)
  The session aborted a request due to an error.
### Monitoring data ingestion
- [PhotogrammetrySession.Output.invalidSample(id:reason:)](photogrammetrysession/output/invalidsample(id:reason:).md)
  A provided sample was invalid.
- [PhotogrammetrySession.Output.automaticDownsampling](photogrammetrysession/output/automaticdownsampling.md)
  The session reduced the image size because of memory constraints.
- [PhotogrammetrySession.Output.skippedSample(id:)](photogrammetrysession/output/skippedsample(id:).md)
  The type of element used for Object Capture updates. The [`PhotogrammetrySample`](photogrammetrysample.md) with the [`id`](photogrammetrysample/id.md) indicated was not able to be used for reconstruction.
### Describing updates
- [var localizedDescription: String](photogrammetrysession/output/localizeddescription.md)
  Localized string containing any extra information about the message, such as the reason why a sample is invalid.
### Iterating outputs
- [PhotogrammetrySession.Outputs.Element](photogrammetrysession/outputs-swift.struct/element.md)
  The type of element used for Photogrammetry Session updates.
- [PhotogrammetrySession.Outputs](photogrammetrysession/outputs-swift.struct.md)
  An asynchronous sequence of session-related updates.
### Structures
- [PhotogrammetrySession.Output.ProgressInfo](photogrammetrysession/output/progressinfo.md)
  ProgressInfo includes the estimated remaining time and the progress stage during reconstruction.
### Enumeration Cases
- [case requestProgressInfo(PhotogrammetrySession.Request, PhotogrammetrySession.Output.ProgressInfo)](photogrammetrysession/output/requestprogressinfo(_:_:).md)
- [PhotogrammetrySession.Output.stitchingIncomplete](photogrammetrysession/output/stitchingincomplete.md)
  The session reconstruction could not fully stitch all images of the object.
### Enumerations
- [PhotogrammetrySession.Output.ProcessingStage](photogrammetrysession/output/processingstage.md)
  Processing stages during reconstruction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var activeRequests: [PhotogrammetrySession.Request]](photogrammetrysession/activerequests.md)
  The session’s active request objects.
- [var isProcessing: Bool](photogrammetrysession/isprocessing.md)
  The session is actively processing requests.
- [var outputs: PhotogrammetrySession.Outputs](photogrammetrysession/outputs-swift.property.md)
  Returns the outputs message stream which can be asynchronously iterated on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output)*