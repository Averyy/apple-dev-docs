# contentTypesForRecentDocuments

**Framework**: UIKit  
**Kind**: property

Content types for browsing recent documents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentTypesForRecentDocuments: [UTType] { get }
```

#### Discussion

The default list is the same as the list of content types you provide to the initializer, or the types you define in [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) in the app’s `Info.plist` file.

You can define a subset of these types using the `UIDocumentBrowserRecentDocumentContentTypes` key in the app’s `Info.plist` file.

## See Also

- [var allowsDocumentCreation: Bool](uidocumentbrowserviewcontroller/allowsdocumentcreation.md)
  A Boolean value that determines whether the document browser can create new documents.
- [var allowsPickingMultipleItems: Bool](uidocumentbrowserviewcontroller/allowspickingmultipleitems.md)
  A Boolean value that determines whether the user can select and open more than one document at a time.
- [func revealDocument(at: URL, importIfNeeded: Bool, completion: ((URL?, (any Error)?) -> Void)?)](uidocumentbrowserviewcontroller/revealdocument(at:importifneeded:completion:).md)
  Reveals, and optionally imports, the document at the provided URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/contenttypesforrecentdocuments)*