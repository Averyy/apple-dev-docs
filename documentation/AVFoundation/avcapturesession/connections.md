# connections

**Framework**: AVFoundation  
**Kind**: property

The connections between inputs and outputs that a capture session contains.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var connections: [AVCaptureConnection] { get }
```

#### Discussion

A capture session automatically forms connections between inputs and outputs when you call the [`addInput(_:)`](avcapturesession/addinput(_:).md) or [`addOutput(_:)`](avcapturesession/addoutput(_:).md) methods. You can explicitly add connections to a session by calling the [`addConnection(_:)`](avcapturesession/addconnection(_:).md) method.

## See Also

- [func addConnection(AVCaptureConnection)](avcapturesession/addconnection(_:).md)
  Adds a connection to the capture session.
- [func canAddConnection(AVCaptureConnection) -> Bool](avcapturesession/canaddconnection(_:).md)
  Determines whether a you can add a connection to a capture session.
- [func addInputWithNoConnections(AVCaptureInput)](avcapturesession/addinputwithnoconnections(_:).md)
  Adds a capture input to a session without forming any connections.
- [func addOutputWithNoConnections(AVCaptureOutput)](avcapturesession/addoutputwithnoconnections(_:).md)
  Adds a capture output to the session without forming any connections.
- [func removeConnection(AVCaptureConnection)](avcapturesession/removeconnection(_:).md)
  Removes a capture connection from the session.
- [class AVCaptureAudioChannel](avcaptureaudiochannel.md)
  An object that monitors average and peak power levels for an audio channel in a capture connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/connections)*