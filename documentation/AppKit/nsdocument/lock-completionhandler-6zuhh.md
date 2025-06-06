# lock(completionHandler:)

**Framework**: AppKit  
**Kind**: method

Prevents the user from making further changes to the document.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func lock() async -> Bool
```

#### Discussion

By default, this method first ensures that any editor who has registered using Cocoa Binding’s NSEditorRegistration informal protocol has committed all changes and then autosaves the document, if necessary, before attempting to lock it using the [`lock(completionHandler:)`](nsdocument/lock(completionhandler:)-161qv.md) method. Upon successful locking, the [`isLocked`](nsdocument/islocked.md) property is set to `[YES]`. Documents whose [`fileURL`](nsdocument/fileurl.md) property is set to `nil` cannot be locked.

## Parameters

- `completionHandler`: The completion handler block object passed in to be invoked after locking is completed, regardless of success or failure of locking.

## See Also

- [func lock(Any?)](nsdocument/lock(_:).md)
  Locks the document in response to the user choosing the Lock menu item.
- [func unlock(Any?)](nsdocument/unlock(_:).md)
  Unlocks the document in response to the user choosing the Unlock menu item.
- [func lock(completionHandler: (((any Error)?) -> Void)?)](nsdocument/lock(completionhandler:)-161qv.md)
  Prevents the user from making changes to the document’s file.
- [func unlock(completionHandler: ((Bool) -> Void)?)](nsdocument/unlock(completionhandler:)-8p8zd.md)
  Allows the user to make modifications to the document.
- [func unlock(completionHandler: (((any Error)?) -> Void)?)](nsdocument/unlock(completionhandler:)-6m7rh.md)
  Allows the user to make modifications to the document’s file.
- [var isLocked: Bool](nsdocument/islocked.md)
  A Boolean value that indicates whether or not the file can be written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/lock(completionhandler:)-6zuhh)*