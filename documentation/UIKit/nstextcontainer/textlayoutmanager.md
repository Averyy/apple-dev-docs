# textLayoutManager

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The [`NSTextLayoutManager`](../nstextlayoutmanager.md) owning the text container.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var textLayoutManager: NSTextLayoutManager? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) NSTextLayoutManager * textLayoutManager;
```

## Discussion

When non-nil, the legacy `layoutManager` should be `nil`.

## See Also

### Managing text components
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The text container’s layout manager.
- [func replaceLayoutManager(NSLayoutManager)](./replacelayoutmanager%28_%29.md)
  Replaces the layout manager for the group of text system objects that contains the text container.
- [var textView: NSTextView?](../../AppKit/nstextcontainer/textview.md)
  The text container’s text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/textlayoutmanager)*