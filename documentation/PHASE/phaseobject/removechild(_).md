# removeChild(_:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Removes the given object as a child.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func removeChild(_ child: PHASEObject)
```

```objc
- (void) removeChild:(PHASEObject *) child;
```

## Parameters

- `child`: The object to remove from the [`children`](./children.md) array.

## See Also

### Managing the Hierarchy
- [var children: [PHASEObject]](./children.md)
  Objects that position and orient in the scene relative to the given object.
- [var parent: PHASEObject?](./parent.md)
  The object that this instance positions and orients relative to in the scene.
- [func addChild(PHASEObject) throws](./addchild%28_%29.md)
  Adds the given object as a child.
- [func removeChildren()](./removechildren%28%29.md)
  Removes all child objects from the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/removechild(_:))*