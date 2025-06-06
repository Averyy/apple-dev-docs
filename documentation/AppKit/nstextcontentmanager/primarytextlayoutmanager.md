# primaryTextLayoutManager

**Framework**: AppKit  
**Kind**: property

The primary text layout manager for this content.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var primaryTextLayoutManager: NSTextLayoutManager? { get set }
```

#### Discussion

Setting this property to an [`NSTextLayoutManager`](nstextlayoutmanager.md) not in `textLayoutManagers` resets it to `nil`. It automatically synchronizes pending edits before switching to a new primary object. The operation is synchronous.

This property is KVO-compliant.

## See Also

- [var textLayoutManagers: [NSTextLayoutManager]](nstextcontentmanager/textlayoutmanagers.md)
  The array of text layout managers associated with this text content manager.
- [var automaticallySynchronizesTextLayoutManagers: Bool](nstextcontentmanager/automaticallysynchronizestextlayoutmanagers.md)
  Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [func addTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/addtextlayoutmanager(_:).md)
  Adds the layout manager you provide to the list of layout managers.
- [func removeTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/removetextlayoutmanager(_:).md)
  Removes the layout manager you specifiy from the list of layout managers.
- [func synchronizeTextLayoutManagers((((any Error)?) -> Void)?)](nstextcontentmanager/synchronizetextlayoutmanagers(_:).md)
  Synchronizes changes to all nonprimary text layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/primarytextlayoutmanager)*