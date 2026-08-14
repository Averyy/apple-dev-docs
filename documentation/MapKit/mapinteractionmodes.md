# MapInteractionModes

**Framework**: MapKit  
**Kind**: struct

Options that indicate the user interactions that the map responds to.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
struct MapInteractionModes
```

#### Overview

A person can’t interact with a map if the option set is empty.

## Topics

### Declared interaction modes
- [static let all: MapInteractionModes](mapinteractionmodes/all.md)
  The map allows all interaction modes.
- [static let pan: MapInteractionModes](mapinteractionmodes/pan.md)
  The map allows a person to pan around to different areas of the map.
- [static let zoom: MapInteractionModes](mapinteractionmodes/zoom.md)
  The map allows people to zoom in or out on map locations.
- [static let pitch: MapInteractionModes](mapinteractionmodes/pitch.md)
  The map allows people to set the map’s pitch to view the map from different angles.
- [static let rotate: MapInteractionModes](mapinteractionmodes/rotate.md)
  The map allows people to rotate the map.
### Creating interaction modes
- [init()](../swift/setalgebra/init.md)
  Creates an empty set.
- [init<S>(S)](../swift/setalgebra/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.ArrayLiteralElement...)](../swift/expressiblebyarrayliteral/init(arrayliteral:).md)
  Creates an instance initialized with the given elements.
- [associatedtype ArrayLiteralElement](../swift/expressiblebyarrayliteral/arrayliteralelement.md)
  The type of the elements of an array literal.
- [associatedtype Element = Self](../swift/optionset/element.md)
  The element type of the option set.
### Accessing members
- [var isEmpty: Bool](../swift/setalgebra/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Comparing sets of modes
- [func contains(Self.Element) -> Bool](../swift/setalgebra/contains(_:).md)
  Returns a Boolean value that indicates whether the given element exists in the set.
- [func isDisjoint(with: Self) -> Bool](../swift/setalgebra/isdisjoint(with:).md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](../swift/setalgebra/isstrictsubset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](../swift/setalgebra/isstrictsuperset(of:).md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](../swift/setalgebra/issubset(of:).md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](../swift/setalgebra/issuperset(of:).md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
### Updating the modes
- [func update(with: Self.Element) -> Self.Element?](../swift/setalgebra/update(with:).md)
  Inserts the given element into the set unconditionally.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](../swift/setalgebra/insert(_:).md)
  Inserts the given element in the set if it is not already present.
- [func remove(Self.Element) -> Self.Element?](../swift/setalgebra/remove(_:).md)
  Removes the given element and any elements subsumed by the given element.
- [func formSymmetricDifference(Self)](../swift/setalgebra/formsymmetricdifference(_:).md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.
- [func subtract(Self)](../swift/setalgebra/subtract(_:).md)
  Removes the elements of the given set from this set.
- [func formUnion(Self)](../swift/setalgebra/formunion(_:).md)
  Adds the elements of the given set to the set.
- [func formIntersection(Self)](../swift/setalgebra/formintersection(_:).md)
  Removes the elements of this set that aren’t also in the given set.
### Combining sets of modes
- [func union(Self) -> Self](../swift/setalgebra/union(_:).md)
  Returns a new set with the elements of both this and the given set.
- [func intersection(Self) -> Self](../swift/setalgebra/intersection(_:).md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func subtracting(Self) -> Self](../swift/setalgebra/subtracting(_:).md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](../swift/setalgebra/symmetricdifference(_:).md)
  Returns a new set with the elements that are either in this set or in the given set, but not in both.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](map/init(bounds:interactionmodes:scope:).md)
  Creates a new, empty map with the bounds, interaction modes, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](map/init(bounds:interactionmodes:scope:content:).md)
  Creates a new map with the bounds, interaction modes, scope, and content you provide.
- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](map/init(bounds:interactionmodes:selection:scope:)-11lec.md)
  Creates a new, empty map with the bounds, interaction modes, a binding to a map feature, and scope you provide.
- [init<SelectedValue>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?)](map/init(bounds:interactionmodes:selection:scope:)-236di.md)
  Creates a new, empty map with the bounds, interaction modes, the selected map feature, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](map/init(bounds:interactionmodes:selection:scope:content:)-28wns.md)
  Creates a new map with the bounds, interaction modes, selected map feature, scope, and map content you provide.
- [init<SelectedValue, C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(bounds:interactionmodes:selection:scope:content:)-2tdbr.md)
  Creates a new map with the bounds, interaction modes, selected value, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](map/init(initialposition:bounds:interactionmodes:scope:).md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](map/init(initialposition:bounds:interactionmodes:scope:content:).md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](map/init(initialposition:bounds:interactionmodes:selection:scope:).md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, selected map feature, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](map/init(initialposition:bounds:interactionmodes:selection:scope:content:)-9feos.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](map/init(initialposition:bounds:interactionmodes:selection:scope:content:)-451vp.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](map/init(position:bounds:interactionmodes:scope:).md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](map/init(position:bounds:interactionmodes:scope:content:).md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](map/init(position:bounds:interactionmodes:selection:scope:).md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](map/init(position:bounds:interactionmodes:selection:scope:content:)-47y4p.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapinteractionmodes)*