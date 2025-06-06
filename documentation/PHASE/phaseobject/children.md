# children

**Framework**: PHASE  
**Kind**: property

Objects that position and orient in the scene relative to the given object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var children: [PHASEObject] { get }
```

#### Discussion

To manage members of this array, use [`addChild(_:)`](phaseobject/addchild(_:).md),  [`removeChild(_:)`](phaseobject/removechild(_:).md), and [`removeChildren()`](phaseobject/removechildren().md).

## See Also

- [var parent: PHASEObject?](phaseobject/parent.md)
  The object that this instance positions and orients relative to in the scene.
- [func addChild(PHASEObject) throws](phaseobject/addchild(_:).md)
  Adds the given object as a child.
- [func removeChild(PHASEObject)](phaseobject/removechild(_:).md)
  Removes the given object as a child.
- [func removeChildren()](phaseobject/removechildren.md)
  Removes all child objects from the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/children)*