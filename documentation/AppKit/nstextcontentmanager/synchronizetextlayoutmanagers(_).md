# synchronizeTextLayoutManagers(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Synchronizes changes to all nonprimary text layout managers.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func synchronizeTextLayoutManagers(_ completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func synchronizeTextLayoutManagers() async throws
```

```objc
- (void) synchronizeTextLayoutManagers:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

If `completionHandler` is `nil`, this method performs the operation synchronously. The framework passes any error to the `completionHandler`. The method blocks (or fails, if synchronous) when there’s an active transaction.

## Parameters

- `completionHandler`: A completion handler that runs on success, or to handle error conditions.

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
- [func removeTextLayoutManager(NSTextLayoutManager)](./removetextlayoutmanager%28_%29.md)
  Removes the layout manager you specifiy from the list of layout managers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanager/synchronizetextlayoutmanagers(_:))*