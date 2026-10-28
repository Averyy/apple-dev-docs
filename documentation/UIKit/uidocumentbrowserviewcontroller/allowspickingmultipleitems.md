# allowsPickingMultipleItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the user can select and open more than one document at a time.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsPickingMultipleItems: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsPickingMultipleItems;
```

## Mentions

- [Customizing the document browser](../customizing-the-browser.md)

## Discussion

By default, this property is set to [`false`](../../Swift/false.md).

## See Also

### Configuring a document browser
- [var allowsDocumentCreation: Bool](./allowsdocumentcreation.md)
  A Boolean value that determines whether the document browser can create new documents.
- [func revealDocument(at: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)?)](./revealdocument%28at,importifneeded,completion%29.md)
  Reveals, and optionally imports, the document at the provided URL.
- [var contentTypesForRecentDocuments: [UTType]](./contenttypesforrecentdocuments.md)
  Content types for browsing recent documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowspickingmultipleitems)*