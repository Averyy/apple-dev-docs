# addInputWithNoConnections(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds a capture input to a session without forming any connections.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
func addInputWithNoConnections(_ input: AVCaptureInput)
```

#### Discussion

You can call this method while the session is running.

In most cases, use the [`addInput(_:)`](avcapturesession/addinput(_:).md) method to add new inputs to a session. Call this method if you require fine-grained control over which inputs connect to which outputs.

## Parameters

- `input`: The capture input to add to the session.

## See Also

- [var connections: [AVCaptureConnection]](avcapturesession/connections.md)
  The connections between inputs and outputs that a capture session contains.
- [func addConnection(AVCaptureConnection)](avcapturesession/addconnection(_:).md)
  Adds a connection to the capture session.
- [func canAddConnection(AVCaptureConnection) -> Bool](avcapturesession/canaddconnection(_:).md)
  Determines whether a you can add a connection to a capture session.
- [func addOutputWithNoConnections(AVCaptureOutput)](avcapturesession/addoutputwithnoconnections(_:).md)
  Adds a capture output to the session without forming any connections.
- [func removeConnection(AVCaptureConnection)](avcapturesession/removeconnection(_:).md)
  Removes a capture connection from the session.
- [class AVCaptureAudioChannel](avcaptureaudiochannel.md)
  An object that monitors average and peak power levels for an audio channel in a capture connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/addinputwithnoconnections(_:))*