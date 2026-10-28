# textView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text container’s text view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
weak var textView: NSTextView? { get set }
```

```objc
@property (weak, nullable) NSTextView * textView;
```

## Discussion

A text container doesn’t need a text view to calculate line fragment rectangles, but must have one to display text.

You can use this property to disconnect a text view from a group of text system objects by sending this message to its text container and passing `nil` as `aTextView`.

## See Also

### Managing text components
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The text container’s layout manager.
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
- [func replaceLayoutManager(NSLayoutManager)](./replacelayoutmanager%28_%29.md)
  Replaces the layout manager for the group of text system objects that contains the text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/textview)*