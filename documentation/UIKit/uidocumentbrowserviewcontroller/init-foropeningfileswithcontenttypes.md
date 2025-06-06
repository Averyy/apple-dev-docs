# init(forOpeningFilesWithContentTypes:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a document browser view controller that can open the specified file types.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(forOpeningFilesWithContentTypes allowedContentTypes: [String]?)
```

## Mentions

- [Customizing the browser](customizing-the-browser.md)

#### Return Value

Returns a newly initialized document browser view controller.

## Parameters

- `allowedContentTypes`: For more information about UTIs, see  .

## See Also

- [var recentDocumentsContentTypes: [String]](uidocumentbrowserviewcontroller/recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [var allowedContentTypes: [String]](uidocumentbrowserviewcontroller/allowedcontenttypes.md)
  The document types that the browser can open.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:).md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:))*