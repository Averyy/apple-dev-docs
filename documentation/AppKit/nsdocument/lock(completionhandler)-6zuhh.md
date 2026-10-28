# lock(completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prevents the user from making further changes to the document.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func lock(completionHandler: ((Bool) -> Void)? = nil)
```

```swift
func lock() async -> Bool
```

```objc
- (void) lockDocumentWithCompletionHandler:(void (^)(BOOL didLock)) completionHandler;
```

## Discussion

By default, this method first ensures that any editor who has registered using Cocoa Binding’s NSEditorRegistration informal protocol has committed all changes and then autosaves the document, if necessary, before attempting to lock it using the [`lock(completionHandler:)`](./lock%28completionhandler%29-161qv.md) method. Upon successful locking, the [`isLocked`](./islocked.md) property is set to `[YES]`. Documents whose [`fileURL`](./fileurl.md) property is set to `nil` cannot be locked.

## Parameters

- `completionHandler`: The completion handler block object passed in to be invoked after locking is completed, regardless of success or failure of locking.

## See Also

### Locking the Document
- [func lock(Any?)](./lock%28_%29.md)
  Locks the document in response to the user choosing the Lock menu item.
- [func unlock(Any?)](./unlock%28_%29.md)
  Unlocks the document in response to the user choosing the Unlock menu item.
- [func lock(completionHandler: (((any Error)?) -> Void)?)](./lock%28completionhandler%29-161qv.md)
  Prevents the user from making changes to the document’s file.
- [func unlock(completionHandler: ((Bool) -> Void)?)](./unlock%28completionhandler%29-8p8zd.md)
  Allows the user to make modifications to the document.
- [func unlock(completionHandler: (((any Error)?) -> Void)?)](./unlock%28completionhandler%29-6m7rh.md)
  Allows the user to make modifications to the document’s file.
- [var isLocked: Bool](./islocked.md)
  A Boolean value that indicates whether or not the file can be written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/lock(completionhandler:)-6zuhh)*