# removeTextLayoutManager(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the layout manager you specifiy from the list of layout managers.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func removeTextLayoutManager(_ textLayoutManager: NSTextLayoutManager)
```

```objc
- (void) removeTextLayoutManager:(NSTextLayoutManager *) textLayoutManager;
```

## Parameters

- `textLayoutManager`: The layout manager to remove.

## See Also

### Working with layout managers
- [var primaryTextLayoutManager: NSTextLayoutManager?](./primarytextlayoutmanager.md)
  The primary text layout manager for this content.
- [var textLayoutManagers: [NSTextLayoutManager]](./textlayoutmanagers.md)
  The array of text layout managers associated with this text content manager.
- [var automaticallySynchronizesTextLayoutManagers: Bool](./automaticallysynchronizestextlayoutmanagers.md)
  Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [func addTextLayoutManager(NSTextLayoutManager)](./addtextlayoutmanager%28_%29.md)
  Adds the layout manager you provide to the list of layout managers.
- [func synchronizeTextLayoutManagers((((any Error)?) -> Void)?)](./synchronizetextlayoutmanagers%28_%29.md)
  Synchronizes changes to all nonprimary text layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/removetextlayoutmanager(_:))*