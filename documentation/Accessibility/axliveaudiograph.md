# AXLiveAudioGraph

**Framework**: Accessibility  
**Kind**: class

An object that represents an audio graph for a live-updating, continuous data series for VoiceOver.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class AXLiveAudioGraph
```

#### Overview

Use [`AXLiveAudioGraph`](axliveaudiograph.md) to interact with an ongoing, continuous stream of data that updates with new data in real time.

## Topics

### Controlling playback
- [class func start()](axliveaudiograph/start.md)
  Begins the live audio graph session.
- [class func stop()](axliveaudiograph/stop.md)
  Ends the live audio graph session.
### Configuring pitch
- [class func updateValue(Double)](axliveaudiograph/updatevalue(_:).md)
  Sets the pitch of the audio graph’s tone.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axliveaudiograph)*