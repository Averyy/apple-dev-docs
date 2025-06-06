# browserUserInterfaceStyle

**Framework**: Uikit  
**Kind**: property

The visual style for the document browser.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var browserUserInterfaceStyle: UIDocumentBrowserViewController.BrowserUserInterfaceStyle { get set }
```

## Mentions

- [Customizing the browser](customizing-the-browser.md)

#### Discussion

For a list of possible styles, see [`UIDocumentBrowserViewController.BrowserUserInterfaceStyle`](uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.enum.md).

> **Note**:  This property has no effect in Mac apps built with Mac Catalyst.

## See Also

- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle](uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.enum.md)
  Styles that define the document browser’s appearance.
- [var additionalLeadingNavigationBarButtonItems: [UIBarButtonItem]](uidocumentbrowserviewcontroller/additionalleadingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [var additionalTrailingNavigationBarButtonItems: [UIBarButtonItem]](uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the trailing side of its navigation bar.
- [var shouldShowFileExtensions: Bool](uidocumentbrowserviewcontroller/shouldshowfileextensions.md)
  A Boolean value that determines whether the browser always shows file extensions.
- [var localizedCreateDocumentActionTitle: String](uidocumentbrowserviewcontroller/localizedcreatedocumentactiontitle.md)
  The title for the Create Document button.
- [var defaultDocumentAspectRatio: CGFloat](uidocumentbrowserviewcontroller/defaultdocumentaspectratio.md)
  The aspect ratio for the Create Document button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property)*