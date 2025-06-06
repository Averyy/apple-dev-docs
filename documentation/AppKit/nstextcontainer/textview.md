# textView

**Framework**: AppKit  
**Kind**: property

The text container’s text view.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var textView: NSTextView? { get set }
```

#### Discussion

A text container doesn’t need a text view to calculate line fragment rectangles, but must have one to display text.

You can use this property to disconnect a text view from a group of text system objects by sending this message to its text container and passing `nil` as `aTextView`.

## See Also

- [var layoutManager: NSLayoutManager?](nstextcontainer/layoutmanager.md)
  The text container’s layout manager.
- [var textLayoutManager: NSTextLayoutManager?](nstextcontainer/textlayoutmanager.md)
- [func replaceLayoutManager(NSLayoutManager)](nstextcontainer/replacelayoutmanager(_:).md)
  Replaces the layout manager for the group of text system objects that contains the text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/textview)*