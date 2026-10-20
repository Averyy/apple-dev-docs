# addTextLayoutManager(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the layout manager you provide to the list of layout managers.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func addTextLayoutManager(_ textLayoutManager: NSTextLayoutManager)
```

```objc
- (void) addTextLayoutManager:(NSTextLayoutManager *) textLayoutManager;
```

## Parameters

- `textLayoutManager`: The layout manager to add.

## See Also

### Working with layout managers
- [var primaryTextLayoutManager: NSTextLayoutManager?](./primarytextlayoutmanager.md)
  The primary text layout manager for this content.
- [var textLayoutManagers: [NSTextLayoutManager]](./textlayoutmanagers.md)
  The array of text layout managers associated with this text content manager.
- [var automaticallySynchronizesTextLayoutManagers: Bool](./automaticallysynchronizestextlayoutmanagers.md)
  Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [func removeTextLayoutManager(NSTextLayoutManager)](./removetextlayoutmanager%28_%29.md)
  Removes the layout manager you specifiy from the list of layout managers.
- [func synchronizeTextLayoutManagers((((any Error)?) -> Void)?)](./synchronizetextlayoutmanagers%28_%29.md)
  Synchronizes changes to all nonprimary text layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/addtextlayoutmanager(_:))*