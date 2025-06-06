# CXPlayDTMFCallAction.ActionType.singleTone

**Framework**: CallKit  
**Kind**: case

Indicates that the user tapped a digit on the in-call keypad.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case singleTone
```

## See Also

- [CXPlayDTMFCallAction.ActionType.softPause](cxplaydtmfcallaction/actiontype/softpause.md)
  Indicates that the user included digits after a soft pause in their dial string. A soft pause is indicated by a comma (`,`) and waits a few seconds before dialing the additional digits.
- [CXPlayDTMFCallAction.ActionType.hardPause](cxplaydtmfcallaction/actiontype/hardpause.md)
  Indicates that the user included digits after a hard pause in their dial string. A hard pause is indicated by a semicolon (`;`) and waits for further user interaction before dialing the additional digits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/actiontype/singletone)*