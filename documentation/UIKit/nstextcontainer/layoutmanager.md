# layoutManager

**Framework**: UIKit  
**Kind**: property

The text container’s layout manager.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get set }
```

#### Discussion

Avoid assigning a layout manager directly through this property. Instead, use the [`replaceLayoutManager(_:)`](nstextcontainer/replacelayoutmanager(_:).md) method when you want to replace the layout manager. The framework sets the value of this property automatically when you add a text container to your layout manager using the [`addTextContainer(_:)`](nslayoutmanager/addtextcontainer(_:).md) method.

## See Also

- [func addTextContainer(NSTextContainer)](nslayoutmanager/addtextcontainer(_:).md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [var textLayoutManager: NSTextLayoutManager?](nstextcontainer/textlayoutmanager.md)
- [func replaceLayoutManager(NSLayoutManager)](nstextcontainer/replacelayoutmanager(_:).md)
  Replaces the layout manager for the group of text system objects that contains the text container.
- [weak var textView: NSTextView? { get set }](../AppKit/NSTextContainer/textView.md)
  The text container’s text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/layoutmanager)*