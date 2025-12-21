# isLocked

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether or not the file can be written to.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var isLocked: Bool { get }
```

#### Discussion

This property may contain the value [`true`](https://developer.apple.com/documentation/Swift/true) because the user lacks the appropriate write permissions, the “user immutable” flag was raised, the parent directory or volume is read only, or the [`checkAutosavingSafety()`](nsdocument/checkautosavingsafety().md) method returned [`false`](https://developer.apple.com/documentation/Swift/false). Do not override this property.

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
- [func unlock(completionHandler: (((any Error)?) -> Void)?)](nsdocument/unlock(completionhandler:)-6m7rh.md)
  Allows the user to make modifications to the document’s file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/islocked)*