# removeChildren()

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeChildren;
```

#### Discussion

This function removes all members from the [`children`](./children.md) array.

## See Also

### Managing the Hierarchy
- [var children: [PHASEObject]](./children.md)
  Objects that position and orient in the scene relative to the given object.
- [var parent: PHASEObject?](./parent.md)
  The object that this instance positions and orients relative to in the scene.
- [func addChild(PHASEObject) throws](./addchild%28_%29.md)
  Adds the given object as a child.
- [func removeChild(PHASEObject)](./removechild%28_%29.md)
  Removes the given object as a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/removechildren())*