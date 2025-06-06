# move(completionHandler:)

**Framework**: AppKit  
**Kind**: method

Moves the document to a user-selected location.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func move() async -> Bool
```

#### Discussion

This method presents the user with a move panel if `[self fileURL]` is non-nil and then tries to save the document to the new location by invoking the [`move(to:completionHandler:)`](nsdocument/move(to:completionhandler:).md) method if the user accepts the location presented by the panel. If a file with the same name already exists at that location, the user will be asked to choose between replacing the pre-existing file, renaming the current document, or canceling the move process. If `[self fileURL]` is `nil`, then the `[self runModalSavePanelForSaveOperation:NSSaveAsOperation delegate:didSaveSelector:contextInfo:]` message is sent instead.

## Parameters

- `completionHandler`: The completion handler block object passed in to be invoked after moving is completed, regardless of success, failure, or cancellation of moving action.

## See Also

- [func moveToUbiquityContainer(Any?)](nsdocument/movetoubiquitycontainer(_:).md)
  Moves the document to the user’s iCloud storage.
- [func move(Any?)](nsdocument/move(_:).md)
  Moves the document to a new location in response to the user choosing the Move To… menu item.
- [func move(to: URL, completionHandler: (((any Error)?) -> Void)?)](nsdocument/move(to:completionhandler:).md)
  Moves the document’s file to the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/move(completionhandler:))*