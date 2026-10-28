# subtype

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Specifies an optional subtype that indicates the direction for the predefined motion-based transitions.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var subtype: CATransitionSubtype? { get set }
```

```objc
@property (copy, nullable) CATransitionSubtype subtype;
```

## Discussion

The possible values are shown in  [Common Transition Subtypes](../common-transition-subtypes.md). The default is `nil`.

This property is ignored if a custom transition is specified in the [`filter`](./filter.md) property.

## See Also

### Transition Properties
- [var type: CATransitionType](./type.md)
  Specifies the predefined transition type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransition/subtype)*