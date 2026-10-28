# replaceLayoutManager(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Replaces the layout manager for the group of text system objects that contains the text container.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func replaceLayoutManager(_ newLayoutManager: NSLayoutManager)
```

```objc
- (void) replaceLayoutManager:(NSLayoutManager *) newLayoutManager;
```

## Discussion

The framework reassigns all text containers and text views attached to the old layout manager to the new layout manager. Unlike setting the [`layoutManager`](./layoutmanager.md) property directly, this method makes all the adjustments necessary to keep the text object relationships intact.

## Parameters

- `newLayoutManager`: The new layout manager.

## See Also

### Managing text components
- [var layoutManager: NSLayoutManager?](./layoutmanager.md)
  The text container’s layout manager.
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
- [var textView: NSTextView?](./textview.md)
  The text container’s text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/replacelayoutmanager(_:))*