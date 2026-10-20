# connections

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<AVCaptureConnection *> * connections;
```

#### Discussion

A capture session automatically forms connections between inputs and outputs when you call the [`addInput(_:)`](./addinput%28_%29.md) or [`addOutput(_:)`](./addoutput%28_%29.md) methods. You can explicitly add connections to a session by calling the [`addConnection(_:)`](./addconnection%28_%29.md) method.

## See Also

### Connecting inputs and outputs
- [func addConnection(AVCaptureConnection)](./addconnection%28_%29.md)
  Adds a connection to the capture session.
- [func canAddConnection(AVCaptureConnection) -> Bool](./canaddconnection%28_%29.md)
  Determines whether a you can add a connection to a capture session.
- [func addInputWithNoConnections(AVCaptureInput)](./addinputwithnoconnections%28_%29.md)
  Adds a capture input to a session without forming any connections.
- [func addOutputWithNoConnections(AVCaptureOutput)](./addoutputwithnoconnections%28_%29.md)
  Adds a capture output to the session without forming any connections.
- [func removeConnection(AVCaptureConnection)](./removeconnection%28_%29.md)
  Removes a capture connection from the session.
- [class AVCaptureAudioChannel](../avcaptureaudiochannel.md)
  An object that monitors average and peak power levels for an audio channel in a capture connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/connections)*