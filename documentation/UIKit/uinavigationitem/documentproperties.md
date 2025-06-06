# documentProperties

**Framework**: UIKit  
**Kind**: property

An object that provides the document header for the title menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var documentProperties: UIDocumentProperties? { get set }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

Assign a non-`nil` value to this property to display a document header at the top of the title menu, which appears when a person taps the navigation item’s title. The document header displays information about the current document, such as its title, file type, and size. Additionally, you can configure a set of sharing capabilities that allow people to share or drag and drop the document content from the document header.

## See Also

- [var titleMenuProvider: (([UIMenuElement]) -> UIMenu?)?](uinavigationitem/titlemenuprovider.md)
  A closure that generates the navigation item’s title menu.
- [class UIDocumentProperties](uidocumentproperties.md)
  Information that UIKit uses to generate a document header for a navigation item’s title menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/documentproperties)*