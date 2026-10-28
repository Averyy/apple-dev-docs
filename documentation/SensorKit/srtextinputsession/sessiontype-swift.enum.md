# SRTextInputSession.SessionType

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

Methods to input text during a session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum SessionType
```

```c
enum SRTextInputSessionType : NSInteger;
```

## Overview

This class defines available options for the [`sessionType`](./sessiontype-swift.property.md) property.

## Topics

### Sources
- [SRTextInputSession.SessionType.dictation](./sessiontype-swift.enum/dictation.md)
  Indicates that the session contains spoken text.
- [SRTextInputSession.SessionType.keyboard](./sessiontype-swift.enum/keyboard.md)
  Indicates that the session contains text from keyboard input.
- [SRTextInputSession.SessionType.pencil](./sessiontype-swift.enum/pencil.md)
  Indicates that the session contains text drawn with Apple Pencil.
- [SRTextInputSession.SessionType.thirdPartyKeyboard](./sessiontype-swift.enum/thirdpartykeyboard.md)
  Indicates that the session contains text from a third-party keyboard.
### Initializers
- [init?(rawValue: Int)](./sessiontype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting Text Source
- [var sessionType: SRTextInputSession.SessionType](./sessiontype-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srtextinputsession/sessiontype-swift.enum)*