# allowsDocumentCreation

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the document browser can create new documents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsDocumentCreation: Bool { get set }
```

## Mentions

- [Customizing the browser](customizing-the-browser.md)

#### Discussion

The browser creates new documents when the user taps the Add (+) button in the navigation bar. The Add button is enabled only if both the [`allowsDocumentCreation`](uidocumentbrowserviewcontroller/allowsdocumentcreation.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true), and the browser delegate implements the [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](uidocumentbrowserviewcontrollerdelegate/documentbrowser(_:didrequestdocumentcreationwithhandler:).md) method.

By default, this property is set to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var allowsPickingMultipleItems: Bool](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md)
  A Boolean value that determines whether the user can select and open more than one document at a time.
- [func revealDocument(at: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)?)](uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:).md)
  Reveals, and optionally imports, the document at the provided URL.
- [var contentTypesForRecentDocuments: [UTType]](uidocumentbrowserviewcontroller/contenttypesforrecentdocuments.md)
  Content types for browsing recent documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowsdocumentcreation)*