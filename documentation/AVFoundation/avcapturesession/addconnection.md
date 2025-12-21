# addConnection(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds a connection to the capture session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
func addConnection(_ connection: AVCaptureConnection)
```

#### Discussion

You can only add a capture connection to a session using this method if [`canAddConnection(_:)`](avcapturesession/canaddconnection(_:).md) returns [`true`](https://developer.apple.com/documentation/Swift/true).

When using [`addInput(_:)`](avcapturesession/addinput(_:).md) or [`addOutput(_:)`](avcapturesession/addoutput(_:).md), the session automatically forms connections between all compatible inputs and outputs. Manually adding connections is only necessary when adding an input or output with no connections.

## Parameters

- `connection`: The capture connection to add to the session.

## See Also

- [var connections: [AVCaptureConnection]](avcapturesession/connections.md)
  The connections between inputs and outputs that a capture session contains.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/addconnection(_:))*