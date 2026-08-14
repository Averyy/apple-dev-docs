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
- [UIControl](../uikit/uicontrol.md)
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
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

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