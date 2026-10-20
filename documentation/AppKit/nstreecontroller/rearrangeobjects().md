# rearrangeObjects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Use this method to trigger reordering of the tree controller’s content.

**Availability**:
- macOS

## Declaration

```swift
func rearrangeObjects()
```

```objc
- (void) rearrangeObjects;
```

#### Discussion

Subclasses should invoke this method if any parameter that affects the arranged objects changes.

## See Also

### Arranging Objects
- [var arrangedObjects: NSTreeNode](./arrangedobjects.md)
  The tree controller’s sorted content objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstreecontroller/rearrangeobjects())*