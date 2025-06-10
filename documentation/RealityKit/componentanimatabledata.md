# ComponentAnimatableData

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ComponentAnimatableData<Root> where Root : Component
```

## Topics

### Initializers
- [init()](componentanimatabledata/init.md)
### Instance Properties
- [var magnitudeSquared: Double](componentanimatabledata/magnitudesquared.md)
### Instance Methods
- [func hasValues() -> Bool](componentanimatabledata/hasvalues.md)
- [func scale(by: Double)](componentanimatabledata/scale(by:).md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct BindPath](bindpath.md)
  The components of a target’s path that refer to the animation properties of a nested scene or entity.
- [enum BindTarget](bindtarget.md)
  A reference to a particular scene, entity, or property that animates.
- [struct BindableValue](bindablevalue.md)
  The value of a bindable target.
- [struct BindableValuesReference](bindablevaluesreference.md)
  A reference to a bindable value of an animation.
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [struct InternalBindPath](internalbindpath.md)
  A bind target for framework-provided properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/componentanimatabledata)*