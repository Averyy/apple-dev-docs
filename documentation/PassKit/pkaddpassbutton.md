# PKAddPassButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

Provides a button that enables users to add passes to Wallet.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class PKAddPassButton
```

```objc
@interface PKAddPassButton : UIButton
```

## Overview

When you use the [`PKAddPassButton`](./pkaddpassbutton.md) class to create a button, you choose the button’s style, and the system provides a control with the correct appearance.

## Topics

### Creating add pass buttons
- [init(addPassButtonStyle: PKAddPassButtonStyle)](./pkaddpassbutton/init%28addpassbuttonstyle%29.md)
  Initializes a new Add Pass button.
- [+ addPassButtonWithStyle:](./pkaddpassbutton/addpassbuttonwithstyle_.md)
  Returns a button that prompts the user to add a pass to Wallet.
### Accessing the button’s style
- [var addPassButtonStyle: PKAddPassButtonStyle](./pkaddpassbutton/addpassbuttonstyle.md)
  A constant representing the button’s style.
### Button styles
- [enum PKAddPassButtonStyle](./pkaddpassbuttonstyle.md)
  The appearance of the buttons that can be created using the [`addPassButtonWithStyle:`](./pkaddpassbutton/addpassbuttonwithstyle_.md) method.

## Relationships

### Inherits From
- [UIButton](../UIKit/uibutton.md)
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
- [UIAccessibilityContentSizeCategoryImageAdjusting](../UIKit/uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](../UIKit/uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Common data types
- [class PKObject](./pkobject.md)
  An opaque type that acts as the superclass for the pass object.
- [class PKLabeledValue](./pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [struct AddPassToWalletButton](./addpasstowalletbutton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct AddPassToWalletButtonFilter](./addpasstowalletbuttonfilter.md)
- [struct AddPassToWalletButtonResponse](./addpasstowalletbuttonresponse.md)
- [struct AddPassToWalletButtonStyle](./addpasstowalletbuttonstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassbutton)*