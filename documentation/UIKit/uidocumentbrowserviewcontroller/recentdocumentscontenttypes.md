# recentDocumentsContentTypes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Content types for browsing recent documents.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`contentTypesForRecentDocuments`](./contenttypesforrecentdocuments.md) instead.

## Declaration

```swift
var recentDocumentsContentTypes: [String] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * recentDocumentsContentTypes;
```

## Discussion

The default list is the same as the list of content types provided to the initializer, or the types defined in [`CFBundleDocumentTypes`](../../BundleResources/information-property-list/cfbundledocumenttypes.md) in the app’s `Info.plist` file.

You can define a subset of these types using the key `UIDocumentBrowserRecentDocumentContentTypes` in the app’s `Info.plist` file.

## See Also

### Deprecated
- [init(forOpeningFilesWithContentTypes: [String]?)](./init%28foropeningfileswithcontenttypes%29.md)
  Initializes and returns a document browser view controller that can open the specified file types.
- [var allowedContentTypes: [String]](./allowedcontenttypes.md)
  The document types that the browser can open.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](./transitioncontroller%28fordocumenturl%29.md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/recentdocumentscontenttypes)*