# replaceLayoutManager(_:)

**Framework**: UIKit  
**Kind**: method

Replaces the layout manager for the group of text system objects that contains the text container.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func replaceLayoutManager(_ newLayoutManager: NSLayoutManager)
```

#### Discussion

The framework reassigns all text containers and text views attached to the old layout manager to the new layout manager. Unlike setting the [`layoutManager`](nstextcontainer/layoutmanager.md) property directly, this method makes all the adjustments necessary to keep the text object relationships intact.

## Parameters

- `newLayoutManager`: The new layout manager.

## See Also

- [var layoutManager: NSLayoutManager?](nstextcontainer/layoutmanager.md)
  The text container’s layout manager.
- [var textLayoutManager: NSTextLayoutManager?](nstextcontainer/textlayoutmanager.md)
- [weak var textView: NSTextView? { get set }](../AppKit/NSTextContainer/textView.md)
  The text container’s text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/replacelayoutmanager(_:))*