# BindableValuesReference

**Framework**: RealityKit  
**Kind**: struct

A reference to a bindable value of an animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct BindableValuesReference
```

#### Overview

As the name indicates, this structure doesn’t exhibit copy-on-write behavior because it’s a reference. This is in contrast to the [`BindableValue`](bindablevalue.md) structure.

## Topics

### Accessing values
- [subscript<T>(BindTarget, T.Type) -> BindableValue<T>?](bindablevaluesreference/subscript(_:_:).md)
  Returns the bindable value at the subscripted index.

## See Also

- [struct BindPath](bindpath.md)
  The components of a target’s path that refer to the animation properties of a nested scene or entity.
- [enum BindTarget](bindtarget.md)
  A reference to a particular scene, entity, or property that animates.
- [struct BindableValue](bindablevalue.md)
  The value of a bindable target.
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [struct InternalBindPath](internalbindpath.md)
  A bind target for framework-provided properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindablevaluesreference)*