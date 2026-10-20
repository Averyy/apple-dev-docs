# AVAudioSessionRouteDescription

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that describes the input and output ports associated with a session’s audio route.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioSessionRouteDescription
```

```objc
@interface AVAudioSessionRouteDescription : NSObject
```

## Mentions

- [Responding to audio route changes](./responding-to-audio-route-changes.md)

#### Overview

You don’t create instances of this class yourself. Instead, you retrieve the current audio route from your app’s [`AVAudioSession`](./avaudiosession.md) object.

## Topics

### Getting the route’s ports
- [var inputs: [AVAudioSessionPortDescription]](./avaudiosessionroutedescription/inputs.md)
  An array of audio input port descriptions.
- [var outputs: [AVAudioSessionPortDescription]](./avaudiosessionroutedescription/outputs.md)
  An array of audio output port descriptions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting the current route
- [var currentRoute: AVAudioSessionRouteDescription](./avaudiosession/currentroute.md)
  A description of the current audio route’s input and output ports.
- [class AVAudioSessionPortDescription](./avaudiosessionportdescription.md)
  Information about the capabilities of the port and the hardware channels it supports.
- [class let routeChangeNotification: NSNotification.Name](./avaudiosession/routechangenotification.md)
  A notification the system posts when its audio route changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionroutedescription)*