# INUIAddVoiceShortcutButton

**Framework**: IntentsUI  
**Kind**: class  
**Role**: Class

A button that allows the user to add or edit a shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class INUIAddVoiceShortcutButton
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface INUIAddVoiceShortcutButton : UIButton
```

*macOS*

```objc
@interface INUIAddVoiceShortcutButton : NSButton
```

#### Overview

When the user performs an action such as placing an order for tomato soup, the app should provide the option to add the action to Siri as a shortcut. To present this option in your app, use [`INUIAddVoiceShortcutButton`](./inuiaddvoiceshortcutbutton.md) to display an “Add to Siri” button. Using this button makes your app consistent with other apps that support Siri Shortcuts.

Set the [`shortcut`](./inuiaddvoiceshortcutbutton/shortcut.md) property on the button to have it automatically update the status of the shortcut. If the user has already added the shortcut to Siri, the button displays “Added” instead of “Add” and includes the phrase that the user chose when adding the shortcut. The methods in [`INUIAddVoiceShortcutButtonDelegate`](./inuiaddvoiceshortcutbuttondelegate.md) aren’t called unless the [`shortcut`](./inuiaddvoiceshortcutbutton/shortcut.md) property is set.

After creating the button, assign its action to a method that displays [`INUIAddVoiceShortcutViewController`](./inuiaddvoiceshortcutviewcontroller.md). This controller guides the user through the process of adding the shortcut to Siri.

The code listing below adds an “Add to Siri” button to a view and lets the user record an invocation phrase

```swift
// Add an "Add to Siri" button to a view.
func addSiriButton(to view: UIView) {
    let button = INUIAddVoiceShortcutButton(style: .blackOutline)
    button.translatesAutoresizingMaskIntoConstraints = false

    view.addSubview(button)
    view.centerXAnchor.constraint(equalTo: button.centerXAnchor).isActive = true
    view.centerYAnchor.constraint(equalTo: button.centerYAnchor).isActive = true

    button.addTarget(self, action: #selector(addToSiri(_:)), for: .touchUpInside)
}

// Present the Add Shortcut view controller after the
// user taps the "Add to Siri" button.
@objc
func addToSiri(_ sender: Any) {
    if let shortcut = INShortcut(intent: orderSoupOfTheDayIntent) {
        let viewController = INUIAddVoiceShortcutViewController(shortcut: shortcut)
        viewController.modalPresentationStyle = .formSheet
        viewController.delegate = self // Object conforming to `INUIAddVoiceShortcutViewControllerDelegate`.
        present(viewController, animated: true, completion: nil)
    }
}

```

## Topics

### Creating a Shortcut Button
- [init(style: INUIAddVoiceShortcutButtonStyle)](./inuiaddvoiceshortcutbutton/init%28style%29.md)
  Creates an *Add to Siri* button with the specified style.
- [enum INUIAddVoiceShortcutButtonStyle](./inuiaddvoiceshortcutbuttonstyle.md)
  The styles for the *Add to Siri* button.
### Presenting Shortcut Editors
- [var shortcut: INShortcut?](./inuiaddvoiceshortcutbutton/shortcut.md)
  The shortcut Siri invokes when the user speaks the invocation phrase.
- [var delegate: (any INUIAddVoiceShortcutButtonDelegate)?](./inuiaddvoiceshortcutbutton/delegate.md)
  The object that receives presentation requests from the button.
- [protocol INUIAddVoiceShortcutButtonDelegate](./inuiaddvoiceshortcutbuttondelegate.md)
  The protocol an object implements to receive notifications from the Siri Shortcut button.
### Accessing Shortcut Button Information
- [func setStyle(INUIAddVoiceShortcutButtonStyle)](./inuiaddvoiceshortcutbutton/setstyle%28_%29.md)
- [var style: INUIAddVoiceShortcutButtonStyle](./inuiaddvoiceshortcutbutton/style.md)
  The button style.
- [var cornerRadius: CGFloat](./inuiaddvoiceshortcutbutton/cornerradius.md)

## Relationships

### Inherits From
- [NSButton](../AppKit/nsbutton.md)
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
- [NSAccessibilityButton](../AppKit/nsaccessibilitybutton.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceCompression](../AppKit/nsuserinterfacecompression.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](../AppKit/nsuserinterfacevalidations.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutbutton)*