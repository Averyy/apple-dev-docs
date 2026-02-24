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
init(forOpeningFilesWithContentTypes allowedContentTypes: [String]?)
```

## Mentions

- [Customizing the document browser](customizing-the-browser.md)

#### Return Value

Returns a newly initialized document browser view controller.

## Parameters

- `allowedContentTypes`: An array of uniform type identifiers (UTIs). The document browser can open only the document types that these UTIs specify.  If you pass `nil`, the browser uses the document types that the `CFBundleDocumentTypes` key specifies in the app’s `Info.plist` file. For detailed instructions about setting the `CFBundleDocumentTypes` key, see the [`Set the supported document types`](setting-up-a-document-browser-app#Set-the-supported-document-types.md) section of [`Setting up a document browser app`](setting-up-a-document-browser-app.md). For more information about UTIs, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers).

## See Also

- [var recentDocumentsContentTypes: [String]](uidocumentbrowserviewcontroller/recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [var allowedContentTypes: [String]](uidocumentbrowserviewcontroller/allowedcontenttypes.md)
  The document types that the browser can open.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:).md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:))*