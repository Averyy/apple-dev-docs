# MapInteractionModes

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

Options that indicate the user interactions that the map responds to.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
struct MapInteractionModes
```

#### Overview

A person can’t interact with a map if the option set is empty.

## Topics

### Declared interaction modes
- [static let all: MapInteractionModes](./mapinteractionmodes/all.md)
  The map allows all interaction modes.
- [static let pan: MapInteractionModes](./mapinteractionmodes/pan.md)
  The map allows a person to pan around to different areas of the map.
- [static let zoom: MapInteractionModes](./mapinteractionmodes/zoom.md)
  The map allows people to zoom in or out on map locations.
- [static let pitch: MapInteractionModes](./mapinteractionmodes/pitch.md)
  The map allows people to set the map’s pitch to view the map from different angles.
- [static let rotate: MapInteractionModes](./mapinteractionmodes/rotate.md)
  The map allows people to rotate the map.
### Creating interaction modes
- [init()](../Swift/setalgebra/init%28%29.md)
  Creates an empty set.
- [init<S>(S)](../Swift/setalgebra/init%28_%29.md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.ArrayLiteralElement...)](../Swift/expressiblebyarrayliteral/init%28arrayliteral%29.md)
  Creates an instance initialized with the given elements.
- [associatedtype ArrayLiteralElement](../Swift/expressiblebyarrayliteral/arrayliteralelement.md)
  The type of the elements of an array literal.
- [associatedtype Element = Self](../Swift/optionset/element.md)
  The element type of the option set.
### Accessing members
- [var isEmpty: Bool](../Swift/setalgebra/isempty.md)
  A Boolean value that indicates whether the set has no elements.
### Comparing sets of modes
- [func contains(Self.Element) -> Bool](../Swift/setalgebra/contains%28_%29.md)
  Returns a Boolean value that indicates whether the given element exists in the set.
- [func isDisjoint(with: Self) -> Bool](../Swift/setalgebra/isdisjoint%28with%29.md)
  Returns a Boolean value that indicates whether the set has no members in common with the given set.
- [func isStrictSubset(of: Self) -> Bool](../Swift/setalgebra/isstrictsubset%28of%29.md)
  Returns a Boolean value that indicates whether this set is a strict subset of the given set.
- [func isStrictSuperset(of: Self) -> Bool](../Swift/setalgebra/isstrictsuperset%28of%29.md)
  Returns a Boolean value that indicates whether this set is a strict superset of the given set.
- [func isSubset(of: Self) -> Bool](../Swift/setalgebra/issubset%28of%29.md)
  Returns a Boolean value that indicates whether the set is a subset of another set.
- [func isSuperset(of: Self) -> Bool](../Swift/setalgebra/issuperset%28of%29.md)
  Returns a Boolean value that indicates whether the set is a superset of the given set.
### Updating the modes
- [func update(with: Self.Element) -> Self.Element?](../Swift/setalgebra/update%28with%29.md)
  Inserts the given element into the set unconditionally.
- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](../Swift/setalgebra/insert%28_%29.md)
  Inserts the given element in the set if it is not already present.
- [func remove(Self.Element) -> Self.Element?](../Swift/setalgebra/remove%28_%29.md)
  Removes the given element and any elements subsumed by the given element.
- [func formSymmetricDifference(Self)](../Swift/setalgebra/formsymmetricdifference%28_%29.md)
  Removes the elements of the set that are also in the given set and adds the members of the given set that are not already in the set.
- [func subtract(Self)](../Swift/setalgebra/subtract%28_%29.md)
  Removes the elements of the given set from this set.
- [func formUnion(Self)](../Swift/setalgebra/formunion%28_%29.md)
  Adds the elements of the given set to the set.
- [func formIntersection(Self)](../Swift/setalgebra/formintersection%28_%29.md)
  Removes the elements of this set that aren’t also in the given set.
### Combining sets of modes
- [func union(Self) -> Self](../Swift/setalgebra/union%28_%29.md)
  Returns a new set with the elements of both this and the given set.
- [func intersection(Self) -> Self](../Swift/setalgebra/intersection%28_%29.md)
  Returns a new set with the elements that are common to both this set and the given set.
- [func subtracting(Self) -> Self](../Swift/setalgebra/subtracting%28_%29.md)
  Returns a new set containing the elements of this set that do not occur in the given set.
- [func symmetricDifference(Self) -> Self](../Swift/setalgebra/symmetricdifference%28_%29.md)
  Returns a new set with the elements that are either in this set or in the given set, but not in both.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Creating a map
- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](./map/init%28bounds,interactionmodes,scope%29.md)
  Creates a new, empty map with the bounds, interaction modes, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](./map/init%28bounds,interactionmodes,scope,content%29.md)
  Creates a new map with the bounds, interaction modes, scope, and content you provide.
- [init(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](./map/init%28bounds,interactionmodes,selection,scope%29-11lec.md)
  Creates a new, empty map with the bounds, interaction modes, a binding to a map feature, and scope you provide.
- [init<SelectedValue>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?)](./map/init%28bounds,interactionmodes,selection,scope%29-236di.md)
  Creates a new, empty map with the bounds, interaction modes, the selected map feature, and scope you provide.
- [init<C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](./map/init%28bounds,interactionmodes,selection,scope,content%29-28wns.md)
  Creates a new map with the bounds, interaction modes, selected map feature, scope, and map content you provide.
- [init<SelectedValue, C>(bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](./map/init%28bounds,interactionmodes,selection,scope,content%29-2tdbr.md)
  Creates a new map with the bounds, interaction modes, selected value, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](./map/init%28initialposition,bounds,interactionmodes,scope%29.md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](./map/init%28initialposition,bounds,interactionmodes,scope,content%29.md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and map content you provide.
- [init(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](./map/init%28initialposition,bounds,interactionmodes,selection,scope%29.md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, selected map feature, and scope you provide.
- [init<C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](./map/init%28initialposition,bounds,interactionmodes,selection,scope,content%29-9feos.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init<SelectedValue, C>(initialPosition: MapCameraPosition, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<SelectedValue?>, scope: Namespace.ID?, content: () -> C)](./map/init%28initialposition,bounds,interactionmodes,selection,scope,content%29-451vp.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected map feature, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?)](./map/init%28position,bounds,interactionmodes,scope%29.md)
  Creates a new, empty map with the initial camera position, bounds, interaction modes, and scope you provide.
- [init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, scope: Namespace.ID?, content: () -> C)](./map/init%28position,bounds,interactionmodes,scope,content%29.md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?)](./map/init%28position,bounds,interactionmodes,selection,scope%29.md)
  Creates a new map with the initial camera position, bounds, interaction modes, scope, and content you provide.
- [init<C>(position: Binding<MapCameraPosition>, bounds: MapCameraBounds?, interactionModes: MapInteractionModes, selection: Binding<MapFeature?>, scope: Namespace.ID?, content: () -> C)](./map/init%28position,bounds,interactionmodes,selection,scope,content%29-47y4p.md)
  Creates a new map with the initial camera position, bounds, interaction modes, selected feature, scope, and content you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapinteractionmodes)*