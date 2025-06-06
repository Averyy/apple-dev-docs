# type

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

The possible values are shown in [`Common Transition Types`](common-transition-types.md). This property is ignored if a custom transition is specified in the [`filter`](catransition/filter.md) property. The default is [`fade`](catransitiontype/fade.md).

## See Also

- [var subtype: CATransitionSubtype?](catransition/subtype.md)
  Specifies an optional subtype that indicates the direction for the predefined motion-based transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransition/type)*