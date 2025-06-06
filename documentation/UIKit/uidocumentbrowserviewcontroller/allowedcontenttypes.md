# allowedContentTypes

**Framework**: UIKit  
**Kind**: property

The document types that the browser can open.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowedContentTypes: [String] { get }
```

#### Discussion

This property contains an array of uniform type identifiers (UTIs). The document browser can open only documents of the types specified by these UTIs.

The list of UTIs is set when the document browser is first created. This list cannot be changed.If you programmatically create a document browser, this list is set to the value passed to the [`init(forOpeningFilesWithContentTypes:)`](uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:).md) method’s `allowedContentTypes` parameter.

If you add a document browser to your project using a storyboard or Interface Builder, this property is calculated based on the the `CFBundleDocumentTypes` key in your app’s `Info.plist` file. For details, see [`Set the supported document types`](setting-up-a-document-browser-app#Set-the-supported-document-types.md).

For more about UTIs, see [`Uniform Type Identifiers Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257).

## See Also

- [init(forOpeningFilesWithContentTypes: [String]?)](uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:).md)
  Initializes and returns a document browser view controller that can open the specified file types.
- [var recentDocumentsContentTypes: [String]](uidocumentbrowserviewcontroller/recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:).md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowedcontenttypes)*