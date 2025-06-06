# removeChildren()

**Framework**: PHASE  
**Kind**: method

Removes all child objects from the given object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func removeChildren()
```

#### Discussion

This function removes all members from the [`children`](phaseobject/children.md) array.

## See Also

- [var children: [PHASEObject]](phaseobject/children.md)
  Objects that position and orient in the scene relative to the given object.
- [var parent: PHASEObject?](phaseobject/parent.md)
  The object that this instance positions and orients relative to in the scene.
- [func addChild(PHASEObject) throws](phaseobject/addchild(_:).md)
  Adds the given object as a child.
- [func removeChild(PHASEObject)](phaseobject/removechild(_:).md)
  Removes the given object as a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/removechildren())*