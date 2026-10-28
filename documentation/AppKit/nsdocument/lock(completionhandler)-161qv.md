# lock(completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prevents the user from making changes to the document’s file.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func lock(completionHandler: (((any Error)?) -> Void)? = nil)
```

```swift
func lock() async throws
```

```objc
- (void) lockWithCompletionHandler:(void (^)(NSError *)) completionHandler;
```

## Discussion

This method first locks the file at `[self fileURL]` and then invokes the given block. The default locking implementation is to enable the “user immutable” flag on the file.

## Parameters

- `completionHandler`: The completion handler block object passed in to be invoked after locking is completed, regardless of success or failure of locking.

## See Also

### Locking the Document
- [func lock(Any?)](./lock%28_%29.md)
  Locks the document in response to the user choosing the Lock menu item.
- [func unlock(Any?)](./unlock%28_%29.md)
  Unlocks the document in response to the user choosing the Unlock menu item.
- [func lock(completionHandler: ((Bool) -> Void)?)](./lock%28completionhandler%29-6zuhh.md)
  Prevents the user from making further changes to the document.
- [func unlock(completionHandler: ((Bool) -> Void)?)](./unlock%28completionhandler%29-8p8zd.md)
  Allows the user to make modifications to the document.
- [func unlock(completionHandler: (((any Error)?) -> Void)?)](./unlock%28completionhandler%29-6m7rh.md)
  Allows the user to make modifications to the document’s file.
- [var isLocked: Bool](./islocked.md)
  A Boolean value that indicates whether or not the file can be written to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/lock(completionhandler:)-161qv)*