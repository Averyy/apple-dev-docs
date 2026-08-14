# AVMetricPlaybackModeSwitchEvent

**Framework**: AVFoundation  
**Kind**: class

Represents a change in playback state, entering one of AVMetricPlaybackMode

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
class AVMetricPlaybackModeSwitchEvent
```

#### Overview

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Identifying the playback mode
- [var mode: AVMetricPlaybackMode](avmetricplaybackmodeswitchevent/mode.md)
  Returns the mode into which playback entered.

## Relationships

### Inherits From
- [AVMetricEvent](avmetricevent.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum AVMetricPlaybackMode](avmetricplaybackmode.md)
  These constants are the possible playback modes returned by the property “mode” on AVMetricPlaybackModeSwitchEvent


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplaybackmodeswitchevent)*