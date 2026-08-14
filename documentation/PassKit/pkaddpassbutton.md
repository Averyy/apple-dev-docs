# PKAddPassButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

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

#### Overview

When you use the [`PKAddPassButton`](pkaddpassbutton.md) class to create a button, you choose the button’s style, and the system provides a control with the correct appearance.

## Topics

### Creating add pass buttons
- [init(addPassButtonStyle: PKAddPassButtonStyle)](pkaddpassbutton/init(addpassbuttonstyle:).md)
  Initializes a new Add Pass button.
### Accessing the button’s style
- [var addPassButtonStyle: PKAddPassButtonStyle](pkaddpassbutton/addpassbuttonstyle.md)
  A constant representing the button’s style.
### Button styles
- [enum PKAddPassButtonStyle](pkaddpassbuttonstyle.md)
  The appearance of the buttons that can be created using the [`addPassButtonWithStyle:`](pkaddpassbutton/addpassbuttonwithstyle:.md) method.

## Relationships

### Inherits From
- [UIButton](../uikit/uibutton.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](../uikit/uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../uikit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](../uikit/uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class PKObject](pkobject.md)
  An opaque type that acts as the superclass for the pass object.
- [class PKLabeledValue](pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [struct AddPassToWalletButton](addpasstowalletbutton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct AddPassToWalletButtonFilter](addpasstowalletbuttonfilter.md)
- [struct AddPassToWalletButtonResponse](addpasstowalletbuttonresponse.md)
- [struct AddPassToWalletButtonStyle](addpasstowalletbuttonstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassbutton)*