# AnimationFillMode

**Framework**: RealityKit  
**Kind**: struct

Options that determine which animation frames display outside of the normal duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct AnimationFillMode
```

#### Overview

This structure enables you to lock an animation at its starting frame for a period of time before beginning. You can also lock an animation to its ending frame for a specified amount of time after it finishes, or both.

An animation applies the fill mode you choose when a range determined by [`trimStart`](animationview/trimstart.md), [`trimEnd`](animationview/trimend.md), or [`trimDuration`](animationview/trimduration.md) exceeds the animation’s underlying duration, which the framework calculates as the frame count (see [`frames`](sampledanimation/frames-2j4nj.md)) multiplied by the [`frameInterval`](sampledanimation/frameinterval.md), multiplied by [`speed`](animationdefinition/speed.md).

For example, if you set the [`trimStart`](animationdefinition/trimstart.md) property for an animation of a hand waving to `-1.0` and [`fillMode`](sampledanimation/fillmode.md) to [`backwards`](animationfillmode/backwards.md) or [`both`](animationfillmode/both.md), the hand displays immediately, freezes at the first animation frame for one second, and then begins to wave.

## Topics

### Choosing a fill mode
- [static let none: AnimationFillMode](animationfillmode/none.md)
  An option that indicates an animation doesn’t display frame data outside of its normal duration.
- [static let forwards: AnimationFillMode](animationfillmode/forwards.md)
  An option that freezes the last frame of the animation until it stops.
- [static let backwards: AnimationFillMode](animationfillmode/backwards.md)
  An option that shows the first animation frame while playback progresses to the beginning position.
- [static let both: AnimationFillMode](animationfillmode/both.md)
  An option that displays the animation’s initial frame or final frame when playback occurs outside of the normal duration.
- [let rawValue: Int8](animationfillmode/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Creating a fill mode
- [init()](animationfillmode/init.md)
  Creates an empty option set.
- [init<S>(S)](animationfillmode/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](animationfillmode/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [init(rawValue: Int8)](animationfillmode/init(rawvalue:).md)
  Creates a fill mode from its backing data type.
### Managing fill mode sets
- [var isEmpty: Bool](animationfillmode/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func contains(Self) -> Bool](animationfillmode/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
- [func formIntersection(Self)](animationfillmode/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func formSymmetricDifference(Self)](animationfillmode/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
- [func formUnion(Self)](animationfillmode/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](animationfillmode/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func intersection(Self) -> Self](animationfillmode/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func isDisjoint(with: Self) -> Bool](animationfillmode/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](animationfillmode/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](animationfillmode/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](animationfillmode/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](animationfillmode/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func remove(Self.Element) -> Self.Element?](animationfillmode/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](animationfillmode/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](animationfillmode/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](animationfillmode/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func union(Self) -> Self](animationfillmode/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func update(with: Self.Element) -> Self.Element?](animationfillmode/update(with:).md)
  Inserts the given element into the set.
### Comparing fill modes
- [static func != (Self, Self) -> Bool](animationfillmode/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Determining the element and raw value type
- [AnimationFillMode.ArrayLiteralElement](animationfillmode/arrayliteralelement.md)
  The type of the elements of an array literal.
- [AnimationFillMode.Element](animationfillmode/element.md)
  The element type of the option set.
- [AnimationFillMode.RawValue](animationfillmode/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](animationfillmode/equatable-implementations.md)
- [OptionSet Implementations](animationfillmode/optionset-implementations.md)
- [SetAlgebra Implementations](animationfillmode/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct SampledAnimation](sampledanimation.md)
  An animation that cycles through a series of frames at a constant interval.
- [enum TweenMode](tweenmode.md)
  Options that determine whether an animation switches between frames gradually or abruptly.
- [struct FromToByAnimation](fromtobyanimation.md)
  An animation that starts, stops, or increments by a specific value.
- [struct AnimationTimingFunction](animationtimingfunction.md)
  The pacing of an animation transition.
- [struct AnimationView](animationview.md)
  An animation that represents a variation of another animation.
- [struct OrbitAnimation](orbitanimation.md)
  An animation that revolves an entity around its origin.
- [protocol AnimationDefinition](animationdefinition.md)
  The configuration, including target object, timeframe, and visual semantics, of an animation.
- [struct AnimationGroup](animationgroup.md)
  A collection of animations that play simultaneously.
- [struct AnimationHandoffType](animationhandofftype.md)
  The type of handoff the play animation method performs between a current animation and a new animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationfillmode)*