# unlock(completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the user to make modifications to the document’s file.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func unlock(completionHandler: (((any Error)?) -> Void)? = nil)
```

```swift
func unlock() async throws
```

```objc
- (void) unlockWithCompletionHandler:(void (^)(NSError *)) completionHandler;
```

#### Discussion

By default, this method tries to clear the “user immutable” flag and, if necessary, add write permissions to the file itself.

## Parameters

- `completionHandler`: The completion handler block object passed in to be invoked after unlocking is completed, regardless of success or failure.

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
- [var isLocked: Bool](./islocked.md)
  A Boolean value that indicates whether or not the file can be written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/unlock(completionhandler:)-6m7rh)*