# unlock(completionHandler:)

**Framework**: AppKit  
**Kind**: method

Allows the user to make modifications to the document’s file.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func unlock() async throws
```

#### Discussion

By default, this method tries to clear the “user immutable” flag and, if necessary, add write permissions to the file itself.

## Parameters

- `completionHandler`: The completion handler block object passed in to be invoked after unlocking is completed, regardless of success or failure.

## See Also

- [func lock(Any?)](nsdocument/lock(_:).md)
  Locks the document in response to the user choosing the Lock menu item.
- [func unlock(Any?)](nsdocument/unlock(_:).md)
  Unlocks the document in response to the user choosing the Unlock menu item.
- [func lock(completionHandler: ((Bool) -> Void)?)](nsdocument/lock(completionhandler:)-6zuhh.md)
  Prevents the user from making further changes to the document.
- [func lock(completionHandler: (((any Error)?) -> Void)?)](nsdocument/lock(completionhandler:)-161qv.md)
  Prevents the user from making changes to the document’s file.
- [func unlock(completionHandler: ((Bool) -> Void)?)](nsdocument/unlock(completionhandler:)-8p8zd.md)
  Allows the user to make modifications to the document.
- [var isLocked: Bool](nsdocument/islocked.md)
  A Boolean value that indicates whether or not the file can be written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/unlock(completionhandler:)-6m7rh)*