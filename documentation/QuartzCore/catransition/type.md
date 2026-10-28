# type

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Specifies the predefined transition type.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var type: CATransitionType { get set }
```

```objc
@property (copy) CATransitionType type;
```

## Discussion

The possible values are shown in [Common Transition Types](../common-transition-types.md). This property is ignored if a custom transition is specified in the [`filter`](./filter.md) property. The default is [`fade`](../catransitiontype/fade.md).

## See Also

### Transition Properties
- [var subtype: CATransitionSubtype?](./subtype.md)
  Specifies an optional subtype that indicates the direction for the predefined motion-based transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransition/type)*