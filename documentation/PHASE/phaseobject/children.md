# children

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSArray<PHASEObject *> * children;
```

#### Discussion

To manage members of this array, use [`addChild(_:)`](./addchild%28_%29.md),  [`removeChild(_:)`](./removechild%28_%29.md), and [`removeChildren()`](./removechildren%28%29.md).

## See Also

### Managing the Hierarchy
- [var parent: PHASEObject?](./parent.md)
  The object that this instance positions and orients relative to in the scene.
- [func addChild(PHASEObject) throws](./addchild%28_%29.md)
  Adds the given object as a child.
- [func removeChild(PHASEObject)](./removechild%28_%29.md)
  Removes the given object as a child.
- [func removeChildren()](./removechildren%28%29.md)
  Removes all child objects from the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseobject/children)*