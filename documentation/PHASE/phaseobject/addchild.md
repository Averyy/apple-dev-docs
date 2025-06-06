# addChild(_:)

**Framework**: PHASE  
**Kind**: method

Adds the given object as a child.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addChild(_ child: PHASEObject) throws
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Discussion

This function throws an error if `child` already has a different parent.

## Parameters

- `child`: The object to add to the   array.

## See Also

- [var children: [PHASEObject]](phaseobject/children.md)
  Objects that position and orient in the scene relative to the given object.
- [var parent: PHASEObject?](phaseobject/parent.md)
  The object that this instance positions and orients relative to in the scene.
- [func removeChild(PHASEObject)](phaseobject/removechild(_:).md)
  Removes the given object as a child.
- [func removeChildren()](phaseobject/removechildren.md)
  Removes all child objects from the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/addchild(_:))*