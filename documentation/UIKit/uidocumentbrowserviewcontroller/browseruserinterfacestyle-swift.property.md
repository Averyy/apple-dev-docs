# browserUserInterfaceStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The visual style for the document browser.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var browserUserInterfaceStyle: UIDocumentBrowserViewController.BrowserUserInterfaceStyle { get set }
```

```objc
@property (nonatomic, assign) UIDocumentBrowserUserInterfaceStyle browserUserInterfaceStyle;
```

## Mentions

- [Customizing the document browser](../customizing-the-browser.md)

#### Discussion

For a list of possible styles, see [`UIDocumentBrowserViewController.BrowserUserInterfaceStyle`](./browseruserinterfacestyle-swift.enum.md).

> **Note**:  This property has no effect in Mac apps built with Mac Catalyst.

## See Also

### Modifying the browser’s appearance
- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle](./browseruserinterfacestyle-swift.enum.md)
  Styles that define the document browser’s appearance.
- [var additionalLeadingNavigationBarButtonItems: [UIBarButtonItem]](./additionalleadingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [var additionalTrailingNavigationBarButtonItems: [UIBarButtonItem]](./additionaltrailingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the trailing side of its navigation bar.
- [var shouldShowFileExtensions: Bool](./shouldshowfileextensions.md)
  A Boolean value that determines whether the browser always shows file extensions.
- [var localizedCreateDocumentActionTitle: String](./localizedcreatedocumentactiontitle.md)
  The title for the Create Document button.
- [var defaultDocumentAspectRatio: CGFloat](./defaultdocumentaspectratio.md)
  The aspect ratio for the Create Document button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.property)*