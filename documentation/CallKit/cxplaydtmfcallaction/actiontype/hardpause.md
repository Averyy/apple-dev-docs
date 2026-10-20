# CXPlayDTMFCallAction.ActionType.hardPause

**Framework**: CallKit  
**Kind**: case  
**Role**: Case

Indicates that the user included digits after a hard pause in their dial string. A hard pause is indicated by a semicolon (`;`) and waits for further user interaction before dialing the additional digits.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case hardPause
```

```c
CXPlayDTMFCallActionTypeHardPause
```

## See Also

### Constants
- [CXPlayDTMFCallAction.ActionType.singleTone](./singletone.md)
  Indicates that the user tapped a digit on the in-call keypad.
- [CXPlayDTMFCallAction.ActionType.softPause](./softpause.md)
  Indicates that the user included digits after a soft pause in their dial string. A soft pause is indicated by a comma (`,`) and waits a few seconds before dialing the additional digits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/actiontype/hardpause)*