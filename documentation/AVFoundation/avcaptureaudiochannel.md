# AVCaptureAudioChannel

**Framework**: AVFoundation  
**Kind**: class

An object that monitors average and peak power levels for an audio channel in a capture connection.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureAudioChannel
```

#### Overview

You don’t create instances of this class directly. Instead, an [`AVCaptureConnection`](avcaptureconnection.md) object that connects an audio input to an audio output provides an array of [`AVCaptureAudioChannel`](avcaptureaudiochannel.md) objects, one for each channel of audio available. You can poll for audio levels by iterating through these audio channel objects.

## Topics

### Configuring a channel
- [var isEnabled: Bool](avcaptureaudiochannel/isenabled.md)
  A Boolean value that indicates whether the channel is in an enabled state.
- [var volume: Float](avcaptureaudiochannel/volume.md)
  The current volume (gain) of the channel.
### Accessing power levels
- [var averagePowerLevel: Float](avcaptureaudiochannel/averagepowerlevel.md)
  The instantaneous average power level in decibels.
- [var peakHoldLevel: Float](avcaptureaudiochannel/peakholdlevel.md)
  The peak hold power level in decibels.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var connections: [AVCaptureConnection]](avcapturesession/connections.md)
  The connections between inputs and outputs that a capture session contains.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel)*