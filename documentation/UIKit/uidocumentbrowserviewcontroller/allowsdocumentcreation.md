# allowsDocumentCreation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the document browser can create new documents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsDocumentCreation: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsDocumentCreation;
```

## Mentions

- [Customizing the document browser](../customizing-the-browser.md)

#### Discussion

The browser creates new documents when the user taps the Add (+) button in the navigation bar. The Add button is enabled only if both the [`allowsDocumentCreation`](./allowsdocumentcreation.md) property is set to [`true`](../../Swift/true.md), and the browser delegate implements the [`documentBrowser(_:didRequestDocumentCreationWithHandler:)`](../uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,didrequestdocumentcreationwithhandler%29.md) method.

By default, this property is set to [`true`](../../Swift/true.md).

## See Also

### Configuring a document browser
- [var allowsPickingMultipleItems: Bool](./allowspickingmultipleitems.md)
  A Boolean value that determines whether the user can select and open more than one document at a time.
- [func revealDocument(at: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)?)](./revealdocument%28at,importifneeded,completion%29.md)
  Reveals, and optionally imports, the document at the provided URL.
- [var contentTypesForRecentDocuments: [UTType]](./contenttypesforrecentdocuments.md)
  Content types for browsing recent documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowsdocumentcreation)*