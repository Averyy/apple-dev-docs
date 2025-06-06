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
@MainActor
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
- [UIButton](../UIKit/UIButton.md)
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
- [UIAccessibilityContentSizeCategoryImageAdjusting](../UIKit/UIAccessibilityContentSizeCategoryImageAdjusting.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/UIContextMenuInteractionDelegate.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UISpringLoadedInteractionSupporting](../UIKit/UISpringLoadedInteractionSupporting.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class PKObject](pkobject.md)
  An opaque type that acts as the superclass for the pass object.
- [class PKLabeledValue](pklabeledvalue.md)
  An object that can represent a detail about a payment card or other item.
- [struct AddPassToWalletButton](addpasstowalletbutton.md)
- [struct AddPassToWalletButtonFilter](addpasstowalletbuttonfilter.md)
- [struct AddPassToWalletButtonResponse](addpasstowalletbuttonresponse.md)
- [struct AddPassToWalletButtonStyle](addpasstowalletbuttonstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassbutton)*