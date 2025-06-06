# synchronizeTextLayoutManagers(_:)

**Framework**: AppKit  
**Kind**: method

Synchronizes changes to all nonprimary text layout managers.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func synchronizeTextLayoutManagers() async throws
```

#### Discussion

If `completionHandler` is `nil`, this method performs the operation synchronously. The framework passes any error to the `completionHandler`. The method blocks (or fails, if synchronous) when there’s an active transaction.

## Parameters

- `completionHandler`: A completion handler that runs on success, or to handle error conditions.

## See Also

- [var primaryTextLayoutManager: NSTextLayoutManager?](nstextcontentmanager/primarytextlayoutmanager.md)
  The primary text layout manager for this content.
- [var textLayoutManagers: [NSTextLayoutManager]](nstextcontentmanager/textlayoutmanagers.md)
  The array of text layout managers associated with this text content manager.
- [var automaticallySynchronizesTextLayoutManagers: Bool](nstextcontentmanager/automaticallysynchronizestextlayoutmanagers.md)
  Determines if the framework should automatically synchronize all text layout managers when exiting an editing transaction.
- [func addTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/addtextlayoutmanager(_:).md)
  Adds the layout manager you provide to the list of layout managers.
- [func removeTextLayoutManager(NSTextLayoutManager)](nstextcontentmanager/removetextlayoutmanager(_:).md)
  Removes the layout manager you specifiy from the list of layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/synchronizetextlayoutmanagers(_:))*