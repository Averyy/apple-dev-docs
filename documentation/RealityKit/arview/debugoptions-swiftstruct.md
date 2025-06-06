# ARView.DebugOptions

**Framework**: RealityKit  
**Kind**: struct

Options for drawing overlay content in a scene that can aid in debugging.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
struct DebugOptions
```

## Topics

### Configuring debug options
- [static let none: ARView.DebugOptions](arview/debugoptions-swift.struct/none.md)
  Disable all debugging overlays.
- [static let showPhysics: ARView.DebugOptions](arview/debugoptions-swift.struct/showphysics.md)
  Draw visualizations for collision objects and rigid bodies.
- [static let showStatistics: ARView.DebugOptions](arview/debugoptions-swift.struct/showstatistics.md)
  Collect performance statistics and display them in the view.
- [static let showAnchorOrigins: ARView.DebugOptions](arview/debugoptions-swift.struct/showanchororigins.md)
  Display anchor origins.
- [static let showAnchorGeometry: ARView.DebugOptions](arview/debugoptions-swift.struct/showanchorgeometry.md)
  Display anchor geometry.
- [static let showWorldOrigin: ARView.DebugOptions](arview/debugoptions-swift.struct/showworldorigin.md)
  Display a coordinate axis indicating the position and orientation of the AR world coordinate system.
- [static let showFeaturePoints: ARView.DebugOptions](arview/debugoptions-swift.struct/showfeaturepoints.md)
  Display a point cloud showing intermediate results of the scene analysis used to track device position.
- [static let showSceneUnderstanding: ARView.DebugOptions](arview/debugoptions-swift.struct/showsceneunderstanding.md)
  Display the depth-colored wireframe for scene-understanding meshes.
### Creating a debug option set
- [init()](arview/debugoptions-swift.struct/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/debugoptions-swift.struct/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](arview/debugoptions-swift.struct/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.DebugOptions.Element](arview/debugoptions-swift.struct/element.md)
  The element type of the option set.
- [ARView.DebugOptions.ArrayLiteralElement](arview/debugoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/debugoptions-swift.struct/init(rawvalue:).md)
  Create a debug options enumeration from a raw value.
- [let rawValue: Int](arview/debugoptions-swift.struct/rawvalue-swift.property.md)
  Options for drawing overlay content in a scene that aids in debugging the scene.
### Testing for membership in a debug option set
- [var isEmpty: Bool](arview/debugoptions-swift.struct/isempty.md)
  A Boolean value that indicates whether the set has no elements.
- [func contains(Self) -> Bool](arview/debugoptions-swift.struct/contains(_:).md)
  Returns a Boolean value that indicates whether a given element is a member of the option set.
### Adding and removing options
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](arview/debugoptions-swift.struct/insert(_:).md)
  Adds the given element to the option set if it is not already a member.
- [func update(with: Self.Element) -> Self.Element?](arview/debugoptions-swift.struct/update(with:).md)
  Inserts the given element into the set.
- [func remove(Self.Element) -> Self.Element?](arview/debugoptions-swift.struct/remove(_:).md)
  Removes the given element and all elements subsumed by it.
- [func subtract(Self)](arview/debugoptions-swift.struct/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func subtracting(Self) -> Self](arview/debugoptions-swift.struct/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
### Combining options
- [func union(Self) -> Self](arview/debugoptions-swift.struct/union(_:).md)
  Returns a new option set of the elements contained in this set, in the given set, or in both.
- [func formUnion(Self)](arview/debugoptions-swift.struct/formunion(_:).md)
  Inserts the elements of another set into this option set.
- [func intersection(Self) -> Self](arview/debugoptions-swift.struct/intersection(_:).md)
  Returns a new option set with only the elements contained in both this set and the given set.
- [func formIntersection(Self)](arview/debugoptions-swift.struct/formintersection(_:).md)
  Removes all elements of this option set that are not also present in the given set.
- [func symmetricDifference(Self) -> Self](arview/debugoptions-swift.struct/symmetricdifference(_:).md)
  Returns a new option set with the elements contained in this set or in the given set, but not in both.
- [func formSymmetricDifference(Self)](arview/debugoptions-swift.struct/formsymmetricdifference(_:).md)
  Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.
### Comparing options
- [static func != (Self, Self) -> Bool](arview/debugoptions-swift.struct/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func isSubset(of: Self) -> Bool](arview/debugoptions-swift.struct/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isStrictSubset(of: Self) -> Bool](arview/debugoptions-swift.struct/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isSuperset(of: Self) -> Bool](arview/debugoptions-swift.struct/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](arview/debugoptions-swift.struct/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isDisjoint(with: Self) -> Bool](arview/debugoptions-swift.struct/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
### Type Aliases
- [ARView.DebugOptions.RawValue](arview/debugoptions-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](arview/debugoptions-swift.struct/equatable-implementations.md)
- [OptionSet Implementations](arview/debugoptions-swift.struct/optionset-implementations.md)
- [SetAlgebra Implementations](arview/debugoptions-swift.struct/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class ARView](arview.md)
  A view that enables you to display an AR experience with RealityKit.
- [typealias ARViewBase](arviewbase.md)
  The platform-specific base class for the view into which RealityKit renders content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct)*