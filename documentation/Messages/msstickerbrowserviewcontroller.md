# MSStickerBrowserViewController

**Framework**: Messages  
**Kind**: class

A view controller that provides dynamic content to the standard sticker browser.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class MSStickerBrowserViewController
```

#### Overview

Use the [`MSStickerBrowserViewController`](msstickerbrowserviewcontroller.md) to present the standard sticker browser. This browser provides drag-and-drop functionality. The user can press and hold a sticker to peel it from the browser, then drag the sticker to any balloon in the transcript. The user can also tap stickers to add them to the Messages app’s input field.

By default, the sticker browser view controller acts as the data source for its [`MSStickerBrowserView`](msstickerbrowserview.md) view (see the [`stickerBrowserView`](msstickerbrowserviewcontroller/stickerbrowserview.md) property). This lets you dynamically change the list of stickers at runtime. You can also customize the size of the stickers inside the browser.

##### Setting the Sticker Browser As Your Root View

To use the sticker browser view controller as your extension’s root view, perform the following steps:

1. Create a custom subclass of the [`MSStickerBrowserViewController`](msstickerbrowserviewcontroller.md) class. For more information, see the subclassing notes.
2. In Interface Builder, add a container view to your extension’s initial scene and pin it to fill the root view as desired. For more information on setting up a container view, see [`Configuring a Container in Interface Builder`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/ImplementingaContainerViewController.html#//apple_ref/doc/uid/TP40007457-CH11-SW20).
3. In the Identity inspector, set the embedded view controller’s class to your custom [`MSStickerBrowserViewController`](msstickerbrowserviewcontroller.md) subclass.

By using an [`MSMessagesAppViewController`](msmessagesappviewcontroller.md) instance as the extension’s root view controller, this approach ensures that the root view controller can respond to important messages from the system, while the contained sticker browser view controller focuses on managing your stickers.

##### Subclassing Notes

By default, this controller sets itself as its sticker browser view’s data source. You must either provide another data source, or implement both [`numberOfStickers(in:)`](msstickerbrowserviewdatasource/numberofstickers(in:).md) and [`stickerBrowserView(_:stickerAt:)`](msstickerbrowserviewdatasource/stickerbrowserview(_:stickerat:).md).

For more information, see [`MSStickerBrowserViewDataSource`](msstickerbrowserviewdatasource.md).

## Topics

### Working with Stickers
- [init(stickerSize: MSStickerSize)](msstickerbrowserviewcontroller/init(stickersize:).md)
  Creates a new sticker browser view controller with stickers of the provided size.
- [var stickerBrowserView: MSStickerBrowserView](msstickerbrowserviewcontroller/stickerbrowserview.md)
  The sticker browser view managed by this controller.
- [var stickerSize: MSStickerSize](msstickerbrowserviewcontroller/stickersize.md)
  A constant that indicates the size of the stickers.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MSStickerBrowserViewDataSource](msstickerbrowserviewdatasource.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)
  Enable your Sticker pack or iMessage app in the media context.
- [Adding your sticker packs to Messages](adding-your-sticker-packs-to-messages.md)
  Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [class MSStickerBrowserView](msstickerbrowserview.md)
  A browser view that displays a dynamically generated list of stickers.
- [class MSStickerView](msstickerview.md)
  A view for displaying a sticker.
- [enum MSStickerSize](msstickersize.md)
  The size of the stickers in the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller)*