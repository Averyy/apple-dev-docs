# value

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The main accessor for the bind value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
var value: T { get set }
```

## Discussion

This property returns the animated value ([`animatedValue`](./animatedvalue.md)) if an animation is active. Otherwise, this property returns the base value ([`baseValue`](./basevalue.md)).

When you assign a value to this property, the setter assigns the value you provide to [`baseValue`](./basevalue.md).

## See Also

### Accessing the value
- [var baseValue: T](./basevalue.md)
  A value that reflects the state of the animated property before or after an animation.
- [var animatedValue: T?](./animatedvalue.md)
  A value that represents the state of the animated property as an animation progresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindablevalue/value)*