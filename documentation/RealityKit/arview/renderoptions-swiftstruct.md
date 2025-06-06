# ARView.RenderOptions

**Framework**: RealityKit  
**Kind**: struct

The available rendering options that you use to selectively disable certain rendering effects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct RenderOptions
```

## Mentions

- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)

#### Overview

RealityKit applies effects to the render make the AR experience more immersive. You can selectively disable any of these effects by adding one or more options from the [`ARView.RenderOptions`](arview/renderoptions-swift.struct.md) set to the view’s [`renderOptions`](arview/renderoptions-swift.property.md) property.

When you initialize a new [`ARView`](arview.md) instance, RealityKit automatically disables certain effects for you, depending on the device hardware. You can change the view’s [`renderOptions`](arview/renderoptions-swift.property.md) to suit your app’s needs, but be sure to consider your app’s GPU utilization when doing so, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

## Topics

### Disabling rendering effects
- [static let disableCameraGrain: ARView.RenderOptions](arview/renderoptions-swift.struct/disablecameragrain.md)
  Disable the image noise effect.
- [static let disableHDR: ARView.RenderOptions](arview/renderoptions-swift.struct/disablehdr.md)
  Disable the high dynamic range post-processing effect.
- [static let disableGroundingShadows: ARView.RenderOptions](arview/renderoptions-swift.struct/disablegroundingshadows.md)
  Disable rendering of ambient occlusion and shadows that ground objects in an AR scene.
- [static let disableMotionBlur: ARView.RenderOptions](arview/renderoptions-swift.struct/disablemotionblur.md)
  Disable the motion blur for all virtual content.
- [static let disableDepthOfField: ARView.RenderOptions](arview/renderoptions-swift.struct/disabledepthoffield.md)
  Disable the depth of field effect for all virtual content.
- [static let disableFaceMesh: ARView.RenderOptions](arview/renderoptions-swift.struct/disablefacemesh.md)
  Disable generation of the face entity with the default occlusion material.
- [static let disablePersonOcclusion: ARView.RenderOptions](arview/renderoptions-swift.struct/disablepersonocclusion.md)
  Disable person segmentation.
- [static let disableAREnvironmentLighting: ARView.RenderOptions](arview/renderoptions-swift.struct/disablearenvironmentlighting.md)
  Disable lighting from environment probes.
- [static let disableFaceOcclusions: ARView.RenderOptions](arview/renderoptions-swift.struct/disablefaceocclusions.md)
  Disable automatic face occlusion.
- [static let disableAutomaticLighting: ARView.RenderOptions](arview/renderoptions-swift.struct/disableautomaticlighting.md)
  Disable automatic updates of the scene lighting.
### Creating an option set
- [init()](arview/renderoptions-swift.struct/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/renderoptions-swift.struct/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](arview/renderoptions-swift.struct/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.RenderOptions.Element](arview/renderoptions-swift.struct/element.md)
  The element type of the option set.
- [ARView.RenderOptions.ArrayLiteralElement](arview/renderoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: UInt)](arview/renderoptions-swift.struct/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [ARView.RenderOptions.RawValue](arview/renderoptions-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [let rawValue: UInt](arview/renderoptions-swift.struct/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Testing for membership in a render option set
- [var isEmpty: Bool](arview/renderoptions-swift.struct/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func contains(Self) -> Bool](arview/renderoptions-swift.struct/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
### Adding and removing options
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](arview/renderoptions-swift.struct/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](arview/renderoptions-swift.struct/update(with:).md)
  Inserts the given element into the set.
- [func remove(Self.Element) -> Self.Element?](arview/renderoptions-swift.struct/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](arview/renderoptions-swift.struct/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](arview/renderoptions-swift.struct/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
### Combining options
- [func union(Self) -> Self](arview/renderoptions-swift.struct/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](arview/renderoptions-swift.struct/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](arview/renderoptions-swift.struct/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](arview/renderoptions-swift.struct/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](arview/renderoptions-swift.struct/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](arview/renderoptions-swift.struct/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
### Comparing options
- [static func != (Self, Self) -> Bool](arview/renderoptions-swift.struct/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Self) -> Bool](arview/renderoptions-swift.struct/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSubset(of: Self) -> Bool](arview/renderoptions-swift.struct/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSuperset(of: Self) -> Bool](arview/renderoptions-swift.struct/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](arview/renderoptions-swift.struct/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isDisjoint(with: Self) -> Bool](arview/renderoptions-swift.struct/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
### Default Implementations
- [Equatable Implementations](arview/renderoptions-swift.struct/equatable-implementations.md)
- [OptionSet Implementations](arview/renderoptions-swift.struct/optionset-implementations.md)
- [SetAlgebra Implementations](arview/renderoptions-swift.struct/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct RealityViewEnvironment](realityviewenvironment.md)
  A struct that determines the background and default lighting properties for a reality view.
- [struct RealityViewRenderingEffects](realityviewrenderingeffects.md)
  A struct for enabling and disabling rendering effects for RealityKit content.
- [struct RealityViewRenderingEffectMode](realityviewrenderingeffectmode.md)
  A mode that determines whether a rendering effect is enabled or disabled.
- [struct RealityViewDynamicRange](realityviewdynamicrange.md)
  Options that determine the state of high dynamic range rendering for virtual content.
- [enum AntialiasingMode](antialiasingmode.md)
  The rendering technique used to smooth edges of virtual content.
- [ARView.Environment](arview/environment-swift.struct.md)
  A description of background, lighting, and acoustic properties for a view’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct)*