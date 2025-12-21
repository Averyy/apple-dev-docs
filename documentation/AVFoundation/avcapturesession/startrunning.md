# startRunning()

**Framework**: AVFoundation  
**Kind**: method

Starts the flow of data through the capture pipeline.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func startRunning()
```

## Mentions

- [Setting up a capture session](setting-up-a-capture-session.md)

#### Discussion

Call this method to start the flow of data from the capture session’s inputs to its outputs. This method is synchronous and blocks until the session starts running or it fails, which it reports by posting an [`runtimeErrorNotification`](avcapturesession/runtimeerrornotification.md) notification.

## See Also

- [func stopRunning()](avcapturesession/stoprunning.md)
  Stops the flow of data through the capture pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/startrunning())*