# AVRoutingPlaybackArbiter

**Framework**: AVRouting  
**Kind**: class  
**Role**: Class

An object that manages playback routing preferences.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+

## Declaration

```swift
class AVRoutingPlaybackArbiter
```

```objc
@interface AVRoutingPlaybackArbiter : NSObject
```

#### Overview

This object manages instances of [`AVRoutingPlaybackParticipant`](./avroutingplaybackparticipant.md) for arbitration of media playback routing priorities and preferences on restricted playback interfaces. The playback routing arbiter is responsible for collecting and applying preferences, such as priorities in non-mixable audio routes and external playback states where the number of allowed players is limited.

## Topics

### Instance Properties
- [var preferredParticipantForExternalPlayback: (any AVRoutingPlaybackParticipant)?](./avroutingplaybackarbiter/preferredparticipantforexternalplayback.md)
  The participant that has priority to play on external playback interfaces.
- [var preferredParticipantForNonMixableAudioRoutes: (any AVRoutingPlaybackParticipant)?](./avroutingplaybackarbiter/preferredparticipantfornonmixableaudioroutes.md)
  The participant that has priority to play audio when it’s not possible to play multiple audio sources concurrently.
### Type Methods
- [class func shared() -> AVRoutingPlaybackArbiter](./avroutingplaybackarbiter/shared%28%29.md)
  Returns the singleton playback arbiter instance.

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

## See Also

### Playback arbitration
- [protocol AVRoutingPlaybackParticipant](./avroutingplaybackparticipant.md)
  A protocol for objects that participate in playback routing arbitration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avroutingplaybackarbiter)*