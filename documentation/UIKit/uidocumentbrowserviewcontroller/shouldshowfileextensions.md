# shouldShowFileExtensions

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the browser always shows file extensions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var shouldShowFileExtensions: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL shouldShowFileExtensions;
```

#### Discussion

The default value is [`false`](../../Swift/false.md).

> **Note**:  This property has no effect in Mac apps built with Mac Catalyst.

## See Also

### Modifying the browser’s appearance
- [var browserUserInterfaceStyle: UIDocumentBrowserViewController.BrowserUserInterfaceStyle](./browseruserinterfacestyle-swift.property.md)
  The visual style for the document browser.
- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle](./browseruserinterfacestyle-swift.enum.md)
  Styles that define the document browser’s appearance.
- [var additionalLeadingNavigationBarButtonItems: [UIBarButtonItem]](./additionalleadingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [var additionalTrailingNavigationBarButtonItems: [UIBarButtonItem]](./additionaltrailingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the trailing side of its navigation bar.
- [var localizedCreateDocumentActionTitle: String](./localizedcreatedocumentactiontitle.md)
  The title for the Create Document button.
- [var defaultDocumentAspectRatio: CGFloat](./defaultdocumentaspectratio.md)
  The aspect ratio for the Create Document button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/shouldshowfileextensions)*