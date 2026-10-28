# MSStickerView

**Framework**: Messages  
**Kind**: class  
**Role**: Class

A view for displaying a sticker.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSStickerView
```

```objc
@interface MSStickerView : UIView
```

## Overview

Use the [`MSStickerView`](./msstickerview.md) class to display stickers. The sticker view also provides drag-and-drop functionality. The user can press and hold a sticker to peel it from the view, and then drag the sticker to any balloon in the transcript.

## Topics

### Working with Sticker Views
- [init(frame: CGRect, sticker: MSSticker?)](./msstickerview/init%28frame,sticker%29.md)
  Initializes a new sticker view with the provided sticker and frame.
- [var sticker: MSSticker?](./msstickerview/sticker.md)
  The displayed sticker object.
### Controlling Sticker Animation
- [var animationDuration: TimeInterval](./msstickerview/animationduration.md)
  The amount of time it takes to complete the sticker’s animation.
- [func isAnimating() -> Bool](./msstickerview/isanimating%28%29.md)
  Returns a Boolean value that indicates whether the sticker is animating.
- [func startAnimating()](./msstickerview/startanimating%28%29.md)
  Starts the sticker’s animation, beginning with the first frame.
- [func stopAnimating()](./msstickerview/stopanimating%28%29.md)
  Stops the sticker’s animation.

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
- [class MSStickerBrowserView](./msstickerbrowserview.md)
  A browser view that displays a dynamically generated list of stickers.
- [enum MSStickerSize](./msstickersize.md)
  The size of the stickers in the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerview)*