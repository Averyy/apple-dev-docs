# InternalBindPath

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A bind target for framework-provided properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS

## Declaration

```swift
struct InternalBindPath
```

## Overview

This structure defines a bind path for the [`BindTarget.internal(_:)`](./bindtarget/internal%28_%29.md) case. As a reference to framework properties, this bind target hides its path. You can, however, store and assign instances of this structure.

## See Also

### Bindable animation targets
- [struct BindPath](./bindpath.md)
  The components of a target’s path that refer to the animation properties of a nested scene or entity.
- [enum BindTarget](./bindtarget.md)
  A reference to a particular scene, entity, or property that animates.
- [struct BindableValue](./bindablevalue.md)
  The value of a bindable target.
- [struct BindableValuesReference](./bindablevaluesreference.md)
  A reference to a bindable value of an animation.
- [struct ParameterSet](./parameterset.md)
  A reference to general-purpose entity parameters for animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/internalbindpath)*