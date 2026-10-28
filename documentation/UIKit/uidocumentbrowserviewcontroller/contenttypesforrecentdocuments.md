# contentTypesForRecentDocuments

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Content types for browsing recent documents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var contentTypesForRecentDocuments: [UTType] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<UTType *> * contentTypesForRecentDocuments;
```

## Discussion

The default list is the same as the list of content types you provide to the initializer, or the types you define in [`CFBundleDocumentTypes`](../../BundleResources/information-property-list/cfbundledocumenttypes.md) in the app’s `Info.plist` file.

You can define a subset of these types using the `UIDocumentBrowserRecentDocumentContentTypes` key in the app’s `Info.plist` file.

## See Also

### Configuring a document browser
- [var allowsDocumentCreation: Bool](./allowsdocumentcreation.md)
  A Boolean value that determines whether the document browser can create new documents.
- [var allowsPickingMultipleItems: Bool](./allowspickingmultipleitems.md)
  A Boolean value that determines whether the user can select and open more than one document at a time.
- [func revealDocument(at: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)?)](./revealdocument%28at,importifneeded,completion%29.md)
  Reveals, and optionally imports, the document at the provided URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/contenttypesforrecentdocuments)*