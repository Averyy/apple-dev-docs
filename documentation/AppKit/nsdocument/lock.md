# lock(_:)

**Framework**: AppKit  
**Kind**: method

Locks the document in response to the user choosing the Lock menu item.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func lock(_ sender: Any?)
```

#### Discussion

This is the action of the Lock menu item in a document-based app. This action method invokes the [`lock(completionHandler:)`](nsdocument/lock(completionhandler:)-6zuhh.md) method by default.

## Parameters

- `sender`: The control sending the message.

## See Also

- [func unlock(Any?)](nsdocument/unlock(_:).md)
  Unlocks the document in response to the user choosing the Unlock menu item.
- [func lock(completionHandler: ((Bool) -> Void)?)](nsdocument/lock(completionhandler:)-6zuhh.md)
  Prevents the user from making further changes to the document.
- [func lock(completionHandler: (((any Error)?) -> Void)?)](nsdocument/lock(completionhandler:)-161qv.md)
  Prevents the user from making changes to the document’s file.
- [func unlock(completionHandler: ((Bool) -> Void)?)](nsdocument/unlock(completionhandler:)-8p8zd.md)
  Allows the user to make modifications to the document.
- [func unlock(completionHandler: (((any Error)?) -> Void)?)](nsdocument/unlock(completionhandler:)-6m7rh.md)
  Allows the user to make modifications to the document’s file.
- [var isLocked: Bool](nsdocument/islocked.md)
  A Boolean value that indicates whether or not the file can be written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/lock(_:))*