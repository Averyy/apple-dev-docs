# addOutputWithNoConnections(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds a capture output to the session without forming any connections.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 2.1+

## Declaration

```swift
func addOutputWithNoConnections(_ output: AVCaptureOutput)
```

```objc
- (void) addOutputWithNoConnections:(AVCaptureOutput *) output;
```

## Discussion

You can call this method while the session is running.

In most cases, use the [`addOutput(_:)`](./addoutput%28_%29.md) method to add new outputs to a session. Call this method if you require fine-grained control over which inputs connect to which outputs.

## Parameters

- `output`: The capture output to add to the session.

## See Also

### Connecting inputs and outputs
- [var connections: [AVCaptureConnection]](./connections.md)
  The connections between inputs and outputs that a capture session contains.
- [func addConnection(AVCaptureConnection)](./addconnection%28_%29.md)
  Adds a connection to the capture session.
- [func canAddConnection(AVCaptureConnection) -> Bool](./canaddconnection%28_%29.md)
  Determines whether a you can add a connection to a capture session.
- [func addInputWithNoConnections(AVCaptureInput)](./addinputwithnoconnections%28_%29.md)
  Adds a capture input to a session without forming any connections.
- [func removeConnection(AVCaptureConnection)](./removeconnection%28_%29.md)
  Removes a capture connection from the session.
- [class AVCaptureAudioChannel](../avcaptureaudiochannel.md)
  An object that monitors average and peak power levels for an audio channel in a capture connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/addoutputwithnoconnections(_:))*