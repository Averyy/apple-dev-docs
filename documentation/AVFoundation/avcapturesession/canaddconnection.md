# canAddConnection(_:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether a you can add a connection to a capture session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
func canAddConnection(_ connection: AVCaptureConnection) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you can add the connection; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `connection`: A connect object to test.

## See Also

- [var connections: [AVCaptureConnection]](avcapturesession/connections.md)
  The connections between inputs and outputs that a capture session contains.
- [func addConnection(AVCaptureConnection)](avcapturesession/addconnection(_:).md)
  Adds a connection to the capture session.
- [func addInputWithNoConnections(AVCaptureInput)](avcapturesession/addinputwithnoconnections(_:).md)
  Adds a capture input to a session without forming any connections.
- [func addOutputWithNoConnections(AVCaptureOutput)](avcapturesession/addoutputwithnoconnections(_:).md)
  Adds a capture output to the session without forming any connections.
- [func removeConnection(AVCaptureConnection)](avcapturesession/removeconnection(_:).md)
  Removes a capture connection from the session.
- [class AVCaptureAudioChannel](avcaptureaudiochannel.md)
  An object that monitors average and peak power levels for an audio channel in a capture connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddconnection(_:))*