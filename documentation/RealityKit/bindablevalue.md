# BindableValue

**Framework**: RealityKit  
**Kind**: struct

The value of a bindable target.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct BindableValue<T> where T : BindableData
```

#### Overview

This structure holds the value of an animatable property ([`animatedValue`](bindablevalue/animatedvalue.md)), that is, the target property that animates. In addition, the structure stores the property’s original value ([`baseValue`](bindablevalue/basevalue.md)), which represents the property’s value before a running animation starts. The [`value`](bindablevalue/value.md) property returns the animated value when an animation runs; when the animation isn’t running, it returns the base value.

## Topics

### Creating a value
- [init(T, animatedValue: T?)](bindablevalue/init(_:animatedvalue:).md)
  Creates a bindable value.
### Accessing the value
- [var value: T](bindablevalue/value.md)
  The main accessor for the bind value.
- [var baseValue: T](bindablevalue/basevalue.md)
  A value that reflects the state of the animated property before or after an animation.
- [var animatedValue: T?](bindablevalue/animatedvalue.md)
  A value that represents the state of the animated property as an animation progresses.

## See Also

- [struct BindPath](bindpath.md)
  The components of a target’s path that refer to the animation properties of a nested scene or entity.
- [enum BindTarget](bindtarget.md)
  A reference to a particular scene, entity, or property that animates.
- [struct BindableValuesReference](bindablevaluesreference.md)
  A reference to a bindable value of an animation.
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [struct InternalBindPath](internalbindpath.md)
  A bind target for framework-provided properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindablevalue)*