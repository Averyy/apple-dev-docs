# representedObject

**Framework**: AppKit  
**Kind**: property

The object represented by the menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
var representedObject: Any? { get set }
```

#### Discussion

By setting a represented object for a menu item, you make an association between the menu item and that object. The represented object functions as a more specific form of tag that allows you to associate any object, not just an arbitrary integer, with the items in a menu.

## See Also

- [var tag: Int](nsmenuitem/tag.md)
  The menu item’s tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/representedobject)*