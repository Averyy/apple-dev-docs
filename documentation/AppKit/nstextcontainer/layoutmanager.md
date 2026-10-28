# layoutManager

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text container’s layout manager.

**Availability**:
- macOS 10.0+

## Declaration

```swift
unowned(unsafe) var layoutManager: NSLayoutManager? { get set }
```

```objc
@property (assign, nullable) NSLayoutManager * layoutManager;
```

## Discussion

Avoid assigning a layout manager directly through this property. Instead, use the [`replaceLayoutManager(_:)`](./replacelayoutmanager%28_%29.md) method when you want to replace the layout manager. The framework sets the value of this property automatically when you add a text container to your layout manager using the [`addTextContainer(_:)`](../nslayoutmanager/addtextcontainer%28_%29.md) method.

## See Also

### Managing text components
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
- [func replaceLayoutManager(NSLayoutManager)](./replacelayoutmanager%28_%29.md)
  Replaces the layout manager for the group of text system objects that contains the text container.
- [var textView: NSTextView?](./textview.md)
  The text container’s text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/layoutmanager)*