# value

**Framework**: RealityKit  
**Kind**: property

The main accessor for the bind value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var value: T { get set }
```

#### Discussion

This property returns the animated value ([`animatedValue`](bindablevalue/animatedvalue.md)) if an animation is active. Otherwise, this property returns the base value ([`baseValue`](bindablevalue/basevalue.md)).

When you assign a value to this property, the setter assigns the value you provide to [`baseValue`](bindablevalue/basevalue.md).

## See Also

- [var baseValue: T](bindablevalue/basevalue.md)
  A value that reflects the state of the animated property before or after an animation.
- [var animatedValue: T?](bindablevalue/animatedvalue.md)
  A value that represents the state of the animated property as an animation progresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindablevalue/value)*