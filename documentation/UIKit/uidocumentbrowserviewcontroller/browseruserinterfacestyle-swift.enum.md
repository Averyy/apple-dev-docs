# UIDocumentBrowserViewController.BrowserUserInterfaceStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Styles that define the document browser’s appearance.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum BrowserUserInterfaceStyle
```

```c
enum UIDocumentBrowserUserInterfaceStyle : NSUInteger;
```

## Topics

### User interface styles
- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle.dark](./browseruserinterfacestyle-swift.enum/dark.md)
  A dark background.
- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle.light](./browseruserinterfacestyle-swift.enum/light.md)
  A light background.
- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle.white](./browseruserinterfacestyle-swift.enum/white.md)
  A white background.
### Initializers
- [init?(rawValue: UInt)](./browseruserinterfacestyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying the browser’s appearance
- [var browserUserInterfaceStyle: UIDocumentBrowserViewController.BrowserUserInterfaceStyle](./browseruserinterfacestyle-swift.property.md)
  The visual style for the document browser.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/browseruserinterfacestyle-swift.enum)*