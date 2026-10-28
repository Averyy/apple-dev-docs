# MSStickerBrowserView

**Framework**: Messages  
**Kind**: class  
**Role**: Class

A browser view that displays a dynamically generated list of stickers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSStickerBrowserView
```

```objc
@interface MSStickerBrowserView : UIView
```

## Overview

Use the [`MSStickerBrowserView`](./msstickerbrowserview.md) to display a dynamically generated list of stickers. The browser provides drag-and-drop functionality. The user can press and hold a sticker to peel it from the browser, then drag the sticker to any balloon in the transcript. The user can also tap stickers to add them to the Messages app’s input field.

The sticker browser presents the stickers provided by its [`dataSource`](./msstickerbrowserview/datasource.md) property. The data source can dynamically change the list of stickers at runtime. You can also customize the size of the stickers inside the browser.

If you create an [`MSStickerBrowserViewController`](./msstickerbrowserviewcontroller.md) object, it automatically creates and displays a sticker browser view with stickers of the specified size. The controller is automatically set as the browser’s data source. Alternatively, you can instantiate your own sticker browser view, letting you customize the size of both the browser and the stickers; however, you need to provide your own data source.

If you need additional customizations, you must build your own user interface using [`MSStickerView`](./msstickerview.md) objects.

If you are simply presenting a static list of stickers using the default browser interface, consider building a Sticker Pack Application instead. For more information, see [Messages](./Messages.md).

## Topics

### Creating Sticker Browser Views
- [init(frame: CGRect)](./msstickerbrowserview/init%28frame%29.md)
  Creates a new sticker browser containing medium-sized stickers.
- [init(frame: CGRect, stickerSize: MSStickerSize)](./msstickerbrowserview/init%28frame,stickersize%29.md)
  Creates a new sticker browser containing stickers of the specified size.
### Managing the Sticker Collection Contents
- [var dataSource: (any MSStickerBrowserViewDataSource)?](./msstickerbrowserview/datasource.md)
  The sticker browser’s data source.
- [protocol MSStickerBrowserViewDataSource](./msstickerbrowserviewdatasource.md)
  The protocol for dynamically providing stickers to a browser view.
- [func reloadData()](./msstickerbrowserview/reloaddata%28%29.md)
  Asks the sticker browser to reload its data from the data source.
### Managing the Browser’s Appearance
- [var contentInset: UIEdgeInsets](./msstickerbrowserview/contentinset.md)
  The distance that the content is inset from the edge of the browser view.
- [var contentOffset: CGPoint](./msstickerbrowserview/contentoffset.md)
  The distance that the content is offset from the browser’s origin.
- [func setContentOffset(CGPoint, animated: Bool)](./msstickerbrowserview/setcontentoffset%28_,animated%29.md)
  Sets the offset distance between the content and the browser’s origin.
- [var stickerSize: MSStickerSize](./msstickerbrowserview/stickersize.md)
  The size of the stickers in the browser.
### Constants
- [enum MSStickerSize](./msstickersize.md)
  The size of the stickers in the browser view.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Custom sticker packs
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](./adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)
  Enable your Sticker pack or iMessage app in the media context.
- [Adding your sticker packs to Messages](./adding-your-sticker-packs-to-messages.md)
  Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [class MSStickerBrowserViewController](./msstickerbrowserviewcontroller.md)
  A view controller that provides dynamic content to the standard sticker browser.
- [class MSStickerView](./msstickerview.md)
  A view for displaying a sticker.
- [enum MSStickerSize](./msstickersize.md)
  The size of the stickers in the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserview)*