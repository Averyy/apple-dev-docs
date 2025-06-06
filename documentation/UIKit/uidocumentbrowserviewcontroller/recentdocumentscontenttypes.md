# recentDocumentsContentTypes

**Framework**: UIKit  
**Kind**: property

Content types for browsing recent documents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var recentDocumentsContentTypes: [String] { get }
```

#### Discussion

The default list is the same as the list of content types provided to the initializer, or the types defined in [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) in the app’s `Info.plist` file.

You can define a subset of these types using the key `UIDocumentBrowserRecentDocumentContentTypes` in the app’s `Info.plist` file.

## See Also

- [init(forOpeningFilesWithContentTypes: [String]?)](uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:).md)
  Initializes and returns a document browser view controller that can open the specified file types.
- [var allowedContentTypes: [String]](uidocumentbrowserviewcontroller/allowedcontenttypes.md)
  The document types that the browser can open.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:).md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/recentdocumentscontenttypes)*