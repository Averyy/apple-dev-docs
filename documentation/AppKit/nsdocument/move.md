# move(_:)

**Framework**: AppKit  
**Kind**: method

Moves the document to a new location in response to the user choosing the Move To… menu item.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func move(_ sender: Any?)
```

#### Discussion

This is the action method of the Move To… menu item in a document-based app. By default, this method invokes the [`move(completionHandler:)`](nsdocument/move(completionhandler:).md) method, passing `nil` as a parameter value.

## Parameters

- `sender`: The control sending the message.

## See Also

- [func move(completionHandler: ((Bool) -> Void)?)](nsdocument/move(completionhandler:).md)
  Moves the document to a user-selected location.
- [func move(to: URL, completionHandler: (((any Error)?) -> Void)?)](nsdocument/move(to:completionhandler:).md)
  Moves the document’s file to the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/move(_:))*