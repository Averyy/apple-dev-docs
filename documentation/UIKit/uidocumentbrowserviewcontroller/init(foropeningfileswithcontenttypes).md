# init(forOpeningFilesWithContentTypes:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a document browser view controller that can open the specified file types.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(forOpening:)`](./init%28foropening%29.md) instead.

## Declaration

```swift
init(forOpeningFilesWithContentTypes allowedContentTypes: [String]?)
```

```objc
- (instancetype) initForOpeningFilesWithContentTypes:(NSArray<NSString *> *) allowedContentTypes;
```

## Mentions

- [Customizing the document browser](../customizing-the-browser.md)

## Return Value

Returns a newly initialized document browser view controller.

## Parameters

- `allowedContentTypes`: An array of uniform type identifiers (UTIs). The document browser can open only the document types that these UTIs specify.  If you pass `nil`, the browser uses the document types that the `CFBundleDocumentTypes` key specifies in the app’s `Info.plist` file.

  For detailed instructions about setting the `CFBundleDocumentTypes` key, see the [Set the supported document types](../setting-up-a-document-browser-app.md#Set-the-supported-document-types) section of [Setting up a document browser app](../setting-up-a-document-browser-app.md).

  For more information about UTIs, see [Uniform Type Identifiers](../../UniformTypeIdentifiers/UniformTypeIdentifiers.md).

## See Also

### Deprecated
- [var recentDocumentsContentTypes: [String]](./recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [var allowedContentTypes: [String]](./allowedcontenttypes.md)
  The document types that the browser can open.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](./transitioncontroller%28fordocumenturl%29.md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/init(foropeningfileswithcontenttypes:))*