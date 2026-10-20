# allowedContentTypes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The document types that the browser can open.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(forOpening:)`](./init%28foropening%29.md) instead.

## Declaration

```swift
var allowedContentTypes: [String] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * allowedContentTypes;
```

#### Discussion

This property contains an array of uniform type identifiers (UTIs). The document browser can open only documents of the types specified by these UTIs.

The list of UTIs is set when the document browser is first created. This list cannot be changed.If you programmatically create a document browser, this list is set to the value passed to the [`init(forOpeningFilesWithContentTypes:)`](./init%28foropeningfileswithcontenttypes%29.md) method’s `allowedContentTypes` parameter.

If you add a document browser to your project using a storyboard or Interface Builder, this property is calculated based on the the `CFBundleDocumentTypes` key in your app’s `Info.plist` file. For details, see [Set the supported document types](../setting-up-a-document-browser-app.md#Set-the-supported-document-types).

For more about UTIs, see [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257).

## See Also

### Deprecated
- [init(forOpeningFilesWithContentTypes: [String]?)](./init%28foropeningfileswithcontenttypes%29.md)
  Initializes and returns a document browser view controller that can open the specified file types.
- [var recentDocumentsContentTypes: [String]](./recentdocumentscontenttypes.md)
  Content types for browsing recent documents.
- [func transitionController(forDocumentURL: URL) -> UIDocumentBrowserTransitionController](./transitioncontroller%28fordocumenturl%29.md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/allowedcontenttypes)*