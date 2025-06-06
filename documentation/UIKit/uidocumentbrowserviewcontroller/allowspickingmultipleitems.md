# allowsPickingMultipleItems

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the user can select and open more than one document at a time.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsPickingMultipleItems: Bool { get set }
```

## Mentions

- [Customizing the browser](customizing-the-browser.md)

#### Discussion

By default, this property is set to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var allowsDocumentCreation: Bool](uidocumentbrowserviewcontroller/allowsdocumentcreation.md)
  A Boolean value that determines whether the document browser can create new documents.
- [func revealDocument(at: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)?)](uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:).md)
  Reveals, and optionally imports, the document at the provided URL.
- [var contentTypesForRecentDocuments: [UTType]](uidocumentbrowserviewcontroller/contenttypesforrecentdocuments.md)
  Content types for browsing recent documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowspickingmultipleitems)*