# layoutManager

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, nullable) NSLayoutManager * layoutManager;
```

## Discussion

Avoid assigning a layout manager directly through this property. Instead, use the [`replaceLayoutManager(_:)`](./replacelayoutmanager%28_%29.md) method when you want to replace the layout manager. The framework sets the value of this property automatically when you add a text container to your layout manager using the [`addTextContainer(_:)`](../nslayoutmanager/addtextcontainer%28_%29.md) method.

## See Also

### Related Documentation
- [func addTextContainer(NSTextContainer)](../nslayoutmanager/addtextcontainer%28_%29.md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
### Managing text components
- [var textLayoutManager: NSTextLayoutManager?](./textlayoutmanager.md)
  The [`NSTextLayoutManager`](../nstextlayoutmanager.md) owning the text container.
- [func replaceLayoutManager(NSLayoutManager)](./replacelayoutmanager%28_%29.md)
  Replaces the layout manager for the group of text system objects that contains the text container.
- [var textView: NSTextView?](../../AppKit/nstextcontainer/textview.md)
  The text container’s text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/layoutmanager)*