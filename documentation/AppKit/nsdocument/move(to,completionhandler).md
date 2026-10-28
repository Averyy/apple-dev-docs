# move(to:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the document’s file to the given URL.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func move(to url: URL, completionHandler: (((any Error)?) -> Void)? = nil)
```

```swift
func move(to url: URL) async throws
```

```objc
- (void) moveToURL:(NSURL *) url completionHandler:(void (^)(NSError *)) completionHandler;
```

## Discussion

The default implementation of this method replaces any file that may currently exist at the given URL with the one being moved, as necessary.

## Parameters

- `url`: The location where the file will ultimately end up, if the move is successful.
- `completionHandler`: The completion handler block object passed in to be invoked at some point in the future, perhaps after the method invocation has returned. The completion handler must be invoked on the main thread. On output, a `nil` error is passed if the move is successful; otherwise an [`NSError`](../../Foundation/nserror.md) object is passed that encapsulates the reason for failure.

## See Also

### Related Documentation
- [func moveToUbiquityContainer(Any?)](./movetoubiquitycontainer%28_%29.md)
  Moves the document to the user’s iCloud storage.
### Moving the Document
- [func move(Any?)](./move%28_%29.md)
  Moves the document to a new location in response to the user choosing the Move To… menu item.
- [func move(completionHandler: ((Bool) -> Void)?)](./move%28completionhandler%29.md)
  Moves the document to a user-selected location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/move(to:completionhandler:))*