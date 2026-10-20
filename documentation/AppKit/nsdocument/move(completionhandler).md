# move(completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the document to a user-selected location.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func move(completionHandler: ((Bool) -> Void)? = nil)
```

```swift
func move() async -> Bool
```

```objc
- (void) moveDocumentWithCompletionHandler:(void (^)(BOOL didMove)) completionHandler;
```

#### Discussion

This method presents the user with a move panel if `[self fileURL]` is non-nil and then tries to save the document to the new location by invoking the [`move(to:completionHandler:)`](./move%28to,completionhandler%29.md) method if the user accepts the location presented by the panel. If a file with the same name already exists at that location, the user will be asked to choose between replacing the pre-existing file, renaming the current document, or canceling the move process. If `[self fileURL]` is `nil`, then the `[self runModalSavePanelForSaveOperation:NSSaveAsOperation delegate:didSaveSelector:contextInfo:]` message is sent instead.

## Parameters

- `completionHandler`: The completion handler block object passed in to be invoked after moving is completed, regardless of success, failure, or cancellation of moving action.

## See Also

### Related Documentation
- [func moveToUbiquityContainer(Any?)](./movetoubiquitycontainer%28_%29.md)
  Moves the document to the user’s iCloud storage.
### Moving the Document
- [func move(Any?)](./move%28_%29.md)
  Moves the document to a new location in response to the user choosing the Move To… menu item.
- [func move(to: URL, completionHandler: (((any Error)?) -> Void)?)](./move%28to,completionhandler%29.md)
  Moves the document’s file to the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/move(completionhandler:))*