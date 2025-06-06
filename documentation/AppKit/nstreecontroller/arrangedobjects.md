# arrangedObjects

**Framework**: AppKit  
**Kind**: property

The tree controller’s sorted content objects.

**Availability**:
- macOS ?+

## Declaration

```swift
var arrangedObjects: NSTreeNode { get }
```

#### Discussion

The value of this property represents a proxy root tree node containing the tree controller’s sorted content objects. The proxy object responds to [`children`](nstreenode/children.md) and [`descendant(at:)`](nstreenode/descendant(at:).md) messages. This property is observable using key-value observing.

## See Also

- [func rearrangeObjects()](nstreecontroller/rearrangeobjects.md)
  Use this method to trigger reordering of the tree controller’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/arrangedobjects)*