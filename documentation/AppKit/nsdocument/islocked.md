# isLocked

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether or not the file can be written to.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var isLocked: Bool { get }
```

```objc
@property (readonly, getter=isLocked) BOOL locked;
```

## Discussion

This property may contain the value [`true`](../../Swift/true.md) because the user lacks the appropriate write permissions, the “user immutable” flag was raised, the parent directory or volume is read only, or the [`checkAutosavingSafety()`](./checkautosavingsafety%28%29.md) method returned [`false`](../../Swift/false.md). Do not override this property.

## See Also

### Locking the Document
- [func lock(Any?)](./lock%28_%29.md)
  Locks the document in response to the user choosing the Lock menu item.
- [func unlock(Any?)](./unlock%28_%29.md)
  Unlocks the document in response to the user choosing the Unlock menu item.
- [func lock(completionHandler: ((Bool) -> Void)?)](./lock%28completionhandler%29-6zuhh.md)
  Prevents the user from making further changes to the document.
- [func lock(completionHandler: (((any Error)?) -> Void)?)](./lock%28completionhandler%29-161qv.md)
  Prevents the user from making changes to the document’s file.
- [func unlock(completionHandler: ((Bool) -> Void)?)](./unlock%28completionhandler%29-8p8zd.md)
  Allows the user to make modifications to the document.
- [func unlock(completionHandler: (((any Error)?) -> Void)?)](./unlock%28completionhandler%29-6m7rh.md)
  Allows the user to make modifications to the document’s file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/islocked)*