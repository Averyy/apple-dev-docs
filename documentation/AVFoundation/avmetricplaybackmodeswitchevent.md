# AVMetricPlaybackModeSwitchEvent

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

Represents a change in playback state, entering one of AVMetricPlaybackMode

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
class AVMetricPlaybackModeSwitchEvent
```

```objc
@interface AVMetricPlaybackModeSwitchEvent : AVMetricEvent
```

## Overview

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Identifying the playback mode
- [var mode: AVMetricPlaybackMode](./avmetricplaybackmodeswitchevent/mode.md)
  Returns the mode into which playback entered.

## Relationships

### Inherits From
- [AVMetricEvent](./avmetricevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Playback mode
- [enum AVMetricPlaybackMode](./avmetricplaybackmode.md)
  These constants are the possible playback modes returned by the property “mode” on AVMetricPlaybackModeSwitchEvent


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplaybackmodeswitchevent)*