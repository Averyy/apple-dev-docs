# ActionButton

**Framework**: MarketplaceKit  
**Kind**: class

A user-interface element that enables a person to install, update, or launch apps by tapping the element.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
@objc @preconcurrency class ActionButton
```

## Mentions

- [Installing apps from an alternative marketplace](installing-apps-from-an-alternative-marketplace.md)
- [Supplying an install verification token](supplying-an-install-verification-token.md)

#### Overview

iOS doesn’t allow an app marketplace to install apps without a person’s consent. When iOS receives a request to install an app, it validates that request came from a user interaction with this button. If instead, a marketplace calls the [`AppLibrary`](applibrary.md) installation methods directly, the call may fail.

## Topics

### Initializers
- [init(action: ActionButton.Action)](actionbutton/init(action:).md)
### Instance Properties
- [let action: ActionButton.Action](actionbutton/action-swift.property.md)
- [var backgroundColor: UIColor?](actionbutton/backgroundcolor.md)
- [var borderColor: UIColor](actionbutton/bordercolor.md)
- [var borderWidth: CGFloat](actionbutton/borderwidth.md)
- [var cornerRadius: CGFloat](actionbutton/cornerradius.md)
- [var fontSize: CGFloat](actionbutton/fontsize.md)
- [var imageName: String?](actionbutton/imagename.md)
- [var imagePlacement: ActionButton.ButtonImagePlacement](actionbutton/imageplacement.md)
- [var isEnabled: Bool](actionbutton/isenabled.md)
- [var isHighlighted: Bool](actionbutton/ishighlighted.md)
- [var label: String](actionbutton/label.md)
- [var size: CGSize](actionbutton/size.md)
- [var tintColor: UIColor!](actionbutton/tintcolor.md)
### Enumerations
- [ActionButton.Action](actionbutton/action-swift.enum.md)
- [ActionButton.ButtonImagePlacement](actionbutton/buttonimageplacement.md)

## Relationships

### Inherits From
- [UIControl](../UIKit/UIControl.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
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
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [struct InstallMetadata](installmetadata.md)
  Information about a specific app to install or update and the person who initiates it.
- [struct InstallConfiguration](installconfiguration.md)
  Information that describes a requested app installation or app update.
- [enum InstallConfirmationResult](installconfirmationresult.md)
  Options that indicate whether the installation of an app proceeds when a person interacts with an app installation button.
- [struct BatchInstallConfiguration](batchinstallconfiguration.md)
  Information that describes multiple app installations or app updates.
- [enum BatchInstallConfirmationResult](batchinstallconfirmationresult.md)
  Options that indicate whether the installation of multiple apps proceeds when a person interacts with an app installation button.
- [enum MarketplaceDisplayOption](marketplacedisplayoption.md)
  The kinds of deep links that the operating system makes into your marketplace.
- [protocol MarketplaceSceneDelegate](marketplacescenedelegate.md)
  A delegate that handles deep link requests into your marketplace app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/actionbutton)*