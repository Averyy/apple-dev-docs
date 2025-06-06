# layoutManager

**Framework**: AppKit  
**Kind**: property

The text container’s layout manager.

**Availability**:
- macOS 10.0+

## Declaration

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get set }
```

#### Discussion

Avoid assigning a layout manager directly through this property. Instead, use the [`replaceLayoutManager(_:)`](nstextcontainer/replacelayoutmanager(_:).md) method when you want to replace the layout manager. The framework sets the value of this property automatically when you add a text container to your layout manager using the [`addTextContainer(_:)`](nslayoutmanager/addtextcontainer(_:).md) method.

## See Also

- [var textLayoutManager: NSTextLayoutManager?](nstextcontainer/textlayoutmanager.md)
- [func replaceLayoutManager(NSLayoutManager)](nstextcontainer/replacelayoutmanager(_:).md)
  Replaces the layout manager for the group of text system objects that contains the text container.
- [var textView: NSTextView?](nstextcontainer/textview.md)
  The text container’s text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/layoutmanager)*