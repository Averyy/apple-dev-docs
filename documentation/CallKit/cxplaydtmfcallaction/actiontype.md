# CXPlayDTMFCallAction.ActionType

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

The types of events that generate dial tones.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum ActionType
```

```c
enum CXPlayDTMFCallActionType : NSInteger;
```

## Topics

### Constants
- [CXPlayDTMFCallAction.ActionType.singleTone](./actiontype/singletone.md)
  Indicates that the user tapped a digit on the in-call keypad.
- [CXPlayDTMFCallAction.ActionType.softPause](./actiontype/softpause.md)
  Indicates that the user included digits after a soft pause in their dial string. A soft pause is indicated by a comma (`,`) and waits a few seconds before dialing the additional digits.
- [CXPlayDTMFCallAction.ActionType.hardPause](./actiontype/hardpause.md)
  Indicates that the user included digits after a hard pause in their dial string. A hard pause is indicated by a semicolon (`;`) and waits for further user interaction before dialing the additional digits.
### Initializers
- [init?(rawValue: Int)](./actiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/actiontype)*