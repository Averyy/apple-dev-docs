# ParameterSet

**Framework**: RealityKit  
**Kind**: struct

A reference to general-purpose entity parameters for animations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct ParameterSet
```

#### Overview

Subscript this structure to access a particular property by name. The return value is [`BindableValue`](bindablevalue.md) `<T>`, where `T` is one of the adopting [`BindableData`](bindabledata.md) types.

As a reference, this structure doesn’t exhibit copy-on-write behavior.

## Topics

### Accessing a parameter by name
- [subscript<T>(String, T.Type) -> BindableValue<T>?](parameterset/subscript(_:_:).md)
  Provides a bindable value for the given name.

## See Also

- [struct BindPath](bindpath.md)
  The components of a target’s path that refer to the animation properties of a nested scene or entity.
- [enum BindTarget](bindtarget.md)
  A reference to a particular scene, entity, or property that animates.
- [struct BindableValue](bindablevalue.md)
  The value of a bindable target.
- [struct BindableValuesReference](bindablevaluesreference.md)
  A reference to a bindable value of an animation.
- [struct InternalBindPath](internalbindpath.md)
  A bind target for framework-provided properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/parameterset)*