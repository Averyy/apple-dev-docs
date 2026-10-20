# canAddConnection(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canAddConnection:(AVCaptureConnection *) connection;
```

#### Return Value

[`true`](../../Swift/true.md) if you can add the connection; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `connection`: A connect object to test.

## See Also

### Connecting inputs and outputs
- [var connections: [AVCaptureConnection]](./connections.md)
  The connections between inputs and outputs that a capture session contains.
- [func addConnection(AVCaptureConnection)](./addconnection%28_%29.md)
  Adds a connection to the capture session.
- [func addInputWithNoConnections(AVCaptureInput)](./addinputwithnoconnections%28_%29.md)
  Adds a capture input to a session without forming any connections.
- [func addOutputWithNoConnections(AVCaptureOutput)](./addoutputwithnoconnections%28_%29.md)
  Adds a capture output to the session without forming any connections.
- [func removeConnection(AVCaptureConnection)](./removeconnection%28_%29.md)
  Removes a capture connection from the session.
- [class AVCaptureAudioChannel](../avcaptureaudiochannel.md)
  An object that monitors average and peak power levels for an audio channel in a capture connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddconnection(_:))*