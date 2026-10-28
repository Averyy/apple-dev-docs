# arrangedObjects

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tree controller’s sorted content objects.

**Availability**:
- macOS

## Declaration

```swift
var arrangedObjects: NSTreeNode { get }
```

```objc
@property (strong, readonly) NSTreeNode * arrangedObjects;
```

## Discussion

The value of this property represents a proxy root tree node containing the tree controller’s sorted content objects. The proxy object responds to [`children`](../nstreenode/children.md) and [`descendant(at:)`](../nstreenode/descendant%28at%29.md) messages. This property is observable using key-value observing.

## See Also

### Arranging Objects
- [func rearrangeObjects()](./rearrangeobjects%28%29.md)
  Use this method to trigger reordering of the tree controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/arrangedobjects)*