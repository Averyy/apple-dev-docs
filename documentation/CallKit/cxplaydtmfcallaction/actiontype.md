# CXPlayDTMFCallAction.ActionType

**Framework**: CallKit  
**Kind**: enum

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

## Topics

### Constants
- [CXPlayDTMFCallAction.ActionType.singleTone](cxplaydtmfcallaction/actiontype/singletone.md)
  Indicates that the user tapped a digit on the in-call keypad.
- [CXPlayDTMFCallAction.ActionType.softPause](cxplaydtmfcallaction/actiontype/softpause.md)
  Indicates that the user included digits after a soft pause in their dial string. A soft pause is indicated by a comma (`,`) and waits a few seconds before dialing the additional digits.
- [CXPlayDTMFCallAction.ActionType.hardPause](cxplaydtmfcallaction/actiontype/hardpause.md)
  Indicates that the user included digits after a hard pause in their dial string. A hard pause is indicated by a semicolon (`;`) and waits for further user interaction before dialing the additional digits.
### Initializers
- [init?(rawValue: Int)](cxplaydtmfcallaction/actiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/actiontype)*