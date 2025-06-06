# MSStickerBrowserView

**Framework**: Messages  
**Kind**: class

A browser view that displays a dynamically generated list of stickers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class MSStickerBrowserView
```

#### Overview

Use the [`MSStickerBrowserView`](msstickerbrowserview.md) to display a dynamically generated list of stickers. The browser provides drag-and-drop functionality. The user can press and hold a sticker to peel it from the browser, then drag the sticker to any balloon in the transcript. The user can also tap stickers to add them to the Messages app’s input field.

The sticker browser presents the stickers provided by its [`dataSource`](msstickerbrowserview/datasource.md) property. The data source can dynamically change the list of stickers at runtime. You can also customize the size of the stickers inside the browser.

If you create an [`MSStickerBrowserViewController`](msstickerbrowserviewcontroller.md) object, it automatically creates and displays a sticker browser view with stickers of the specified size. The controller is automatically set as the browser’s data source. Alternatively, you can instantiate your own sticker browser view, letting you customize the size of both the browser and the stickers; however, you need to provide your own data source.

If you need additional customizations, you must build your own user interface using [`MSStickerView`](msstickerview.md) objects.

If you are simply presenting a static list of stickers using the default browser interface, consider building a Sticker Pack Application instead. For more information, see [`Messages`](Messages.md).

## Topics

### Creating Sticker Browser Views
- [init(frame: CGRect)](msstickerbrowserview/init(frame:).md)
  Creates a new sticker browser containing medium-sized stickers.
- [init(frame: CGRect, stickerSize: MSStickerSize)](msstickerbrowserview/init(frame:stickersize:).md)
  Creates a new sticker browser containing stickers of the specified size.
### Managing the Sticker Collection Contents
- [var dataSource: (any MSStickerBrowserViewDataSource)?](msstickerbrowserview/datasource.md)
  The sticker browser’s data source.
- [protocol MSStickerBrowserViewDataSource](msstickerbrowserviewdatasource.md)
  The protocol for dynamically providing stickers to a browser view.
- [func reloadData()](msstickerbrowserview/reloaddata.md)
  Asks the sticker browser to reload its data from the data source.
### Managing the Browser’s Appearance
- [var contentInset: UIEdgeInsets](msstickerbrowserview/contentinset.md)
  The distance that the content is inset from the edge of the browser view.
- [var contentOffset: CGPoint](msstickerbrowserview/contentoffset.md)
  The distance that the content is offset from the browser’s origin.
- [func setContentOffset(CGPoint, animated: Bool)](msstickerbrowserview/setcontentoffset(_:animated:).md)
  Sets the offset distance between the content and the browser’s origin.
- [var stickerSize: MSStickerSize](msstickerbrowserview/stickersize.md)
  The size of the stickers in the browser.
### Constants
- [enum MSStickerSize](msstickersize.md)
  The size of the stickers in the browser view.

## Relationships

### Inherits From
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)
  Enable your Sticker pack or iMessage app in the media context.
- [Adding your sticker packs to Messages](adding-your-sticker-packs-to-messages.md)
  Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [class MSStickerBrowserViewController](msstickerbrowserviewcontroller.md)
  A view controller that provides dynamic content to the standard sticker browser.
- [class MSStickerView](msstickerview.md)
  A view for displaying a sticker.
- [enum MSStickerSize](msstickersize.md)
  The size of the stickers in the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview)*