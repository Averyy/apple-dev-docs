# type

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The type of the call action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var type: CXPlayDTMFCallAction.ActionType { get set }
```

```objc
@property (nonatomic) CXPlayDTMFCallActionType type;
```

#### Discussion

For possible values, see [`CXPlayDTMFCallAction.ActionType`](./actiontype.md).

## See Also

### Accessing Action Information
- [var digits: String](./digits.md)
  The digits tapped by the user into the in-call keypad or included in the dial string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction/type)*