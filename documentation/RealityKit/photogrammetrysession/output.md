# PhotogrammetrySession.Output

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

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

- [Creating 3D objects from photographs](../creating-3d-objects-from-photographs.md)

## Overview

RealityKit’s Object Capture is a long-running background task. The session publishes messages status and error messages to [`outputs`](./outputs-swift.property.md), a Swift [`AsyncSequence`](../../Swift/asyncsequence.md).

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
- [PhotogrammetrySession.Output.inputComplete](./output/inputcomplete.md)
  The data ingestion portion of the process is complete.
- [PhotogrammetrySession.Output.processingComplete](./output/processingcomplete.md)
  The session completed a request successfully.
- [PhotogrammetrySession.Output.processingCancelled](./output/processingcancelled.md)
  All pending requests are canceled.
### Monitoring request status
- [case requestProgress(PhotogrammetrySession.Request, fractionComplete: Double)](./output/requestprogress%28_,fractioncomplete%29.md)
  A progress update provided by the session.
- [case requestComplete(PhotogrammetrySession.Request, PhotogrammetrySession.Result)](./output/requestcomplete%28_,_%29.md)
  The session finished handling all pending requests.
- [case requestError(PhotogrammetrySession.Request, any Error)](./output/requesterror%28_,_%29.md)
  The session aborted a request due to an error.
### Monitoring data ingestion
- [PhotogrammetrySession.Output.invalidSample(id:reason:)](./output/invalidsample%28id,reason%29.md)
  A provided sample was invalid.
- [PhotogrammetrySession.Output.automaticDownsampling](./output/automaticdownsampling.md)
  The session reduced the image size because of memory constraints.
- [PhotogrammetrySession.Output.skippedSample(id:)](./output/skippedsample%28id%29.md)
  The type of element used for Object Capture updates. The [`PhotogrammetrySample`](../photogrammetrysample.md) with the [`id`](../photogrammetrysample/id.md) indicated was not able to be used for reconstruction.
### Describing updates
- [var localizedDescription: String](./output/localizeddescription.md)
  Localized string containing any extra information about the message, such as the reason why a sample is invalid.
### Iterating outputs
- [PhotogrammetrySession.Outputs](./outputs-swift.struct.md)
  An asynchronous sequence of session-related updates.
### Structures
- [PhotogrammetrySession.Output.ProgressInfo](./output/progressinfo.md)
  ProgressInfo includes the estimated remaining time and the progress stage during reconstruction.
### Enumeration Cases
- [case requestProgressInfo(PhotogrammetrySession.Request, PhotogrammetrySession.Output.ProgressInfo)](./output/requestprogressinfo%28_,_%29.md)
- [PhotogrammetrySession.Output.stitchingIncomplete](./output/stitchingincomplete.md)
  The session reconstruction could not fully stitch all images of the object.
### Enumerations
- [PhotogrammetrySession.Output.ProcessingStage](./output/processingstage.md)
  Processing stages during reconstruction.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitoring the session
- [var activeRequests: [PhotogrammetrySession.Request]](./activerequests.md)
  The session’s active request objects.
- [var isProcessing: Bool](./isprocessing.md)
  The session is actively processing requests.
- [var outputs: PhotogrammetrySession.Outputs](./outputs-swift.property.md)
  Returns the outputs message stream which can be asynchronously iterated on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output)*