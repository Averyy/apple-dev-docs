# automaticallySynchronizesTextLayoutManagers

**Framework**: UIKit  
**Kind**: property

Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var automaticallySynchronizesTextLayoutManagers: Bool { get set }
```

## See Also

- [var primaryTextLayoutManager: NSTextLayoutManager?](nstextcontentmanager/primarytextlayoutmanager.md)
  The primary text layout manager for this content.
- [var textLayoutManagers: [NSTextLayoutManager]](nstextcontentmanager/textlayoutmanagers.md)
  The array of text layout managers associated with this text content manager.
- [func addTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/addtextlayoutmanager(_:).md)
  Adds the layout manager you provide to the list of layout managers.
- [func removeTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/removetextlayoutmanager(_:).md)
  Removes the layout manager you specifiy from the list of layout managers.
- [func synchronizeTextLayoutManagers((((any Error)?) -> Void)?)](nstextcontentmanager/synchronizetextlayoutmanagers(_:).md)
  Synchronizes changes to all nonprimary text layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentmanager/automaticallysynchronizestextlayoutmanagers)*