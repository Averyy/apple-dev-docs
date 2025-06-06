# moveToUbiquityContainer(_:)

**Framework**: AppKit  
**Kind**: method

Moves the document to the user’s iCloud storage.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@IBAction
@MainActor func moveToUbiquityContainer(_ sender: Any?)
```

#### Discussion

AppKit calls this method automatically in response to the user selecting the Move to iCloud… menu item in a document-based app. The default implementation presents the user with an alert asking to confirm the move before invoking the [`move(to:completionHandler:)`](nsdocument/move(to:completionhandler:).md) method with a URL in the app’s default ubiquity container.

See Moving the Document for descriptions of methods for moving a document to a local path.

## Parameters

- `sender`: The control sending the message.

## See Also

- [class var usesUbiquitousStorage: Bool](nsdocument/usesubiquitousstorage.md)
  Returns whether the document object stores its contents in the user’s iCloud document storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/movetoubiquitycontainer(_:))*