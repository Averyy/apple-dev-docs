# additionalTrailingNavigationBarButtonItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Additional bar button items that the document browser displays on the trailing side of its navigation bar.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var additionalTrailingNavigationBarButtonItems: [UIBarButtonItem] { get set }
```

```objc
@property (nonatomic, strong) NSArray<UIBarButtonItem *> * additionalTrailingNavigationBarButtonItems;
```

## Mentions

- [Adding custom actions and activities](../adding-custom-actions-and-activities.md)

## Discussion

Actions triggered by these items don’t have any access to the browser’s content or to the URLs of selected items. Use these bar button items for global actions only (actions that don’t affect a specific document or folder).

> **Note**:  Bar button items added using this property don’t appear in Mac apps built with Mac Catalyst. You must find another way to display these actions (for example, using [`UIMenuBuilder`](../uimenubuilder.md) to add the actions to your app’s menu).

## See Also

### Modifying the browser’s appearance
- [var browserUserInterfaceStyle: UIDocumentBrowserViewController.BrowserUserInterfaceStyle](./browseruserinterfacestyle-swift.property.md)
  The visual style for the document browser.
- [UIDocumentBrowserViewController.BrowserUserInterfaceStyle](./browseruserinterfacestyle-swift.enum.md)
  Styles that define the document browser’s appearance.
- [var additionalLeadingNavigationBarButtonItems: [UIBarButtonItem]](./additionalleadingnavigationbarbuttonitems.md)
  Additional bar button items that the document browser displays on the leading side of its navigation bar.
- [var shouldShowFileExtensions: Bool](./shouldshowfileextensions.md)
  A Boolean value that determines whether the browser always shows file extensions.
- [var localizedCreateDocumentActionTitle: String](./localizedcreatedocumentactiontitle.md)
  The title for the Create Document button.
- [var defaultDocumentAspectRatio: CGFloat](./defaultdocumentaspectratio.md)
  The aspect ratio for the Create Document button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/additionaltrailingnavigationbarbuttonitems)*