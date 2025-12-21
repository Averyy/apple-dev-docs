# UIFontPickerViewController

**Framework**: UIKit  
**Kind**: class

A view controller that manages the interface for selecting a font that the system provides or the user installs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFontPickerViewController
```

#### Overview

Use a [`UIFontPickerViewController`](uifontpickerviewcontroller.md) to provide the user access to all the fonts on their device. Directly querying [`UIFont`](uifont.md) provides only system fonts, but the user may have additional fonts on their device. When the user selects one of these nonsystem fonts in the font picker, the system grants your app access to the font.

The font picker has several customization options collected into a [`UIFontPickerViewController.Configuration`](uifontpickerviewcontroller/configuration-swift.class.md) object. For example, you can set [`includeFaces`](uifontpickerviewcontroller/configuration-swift.class/includefaces.md) to [`true`](https://developer.apple.com/documentation/Swift/true) so that the user can select not only the font but a bold or italic face within that font family. Customize the configuration object first, then pass it as an argument in the font picker’s [`init(configuration:)`](uifontpickerviewcontroller/init(configuration:).md) method.

```swift
    func showFontPicker(_ sender: Any) {
        let fontConfig = UIFontPickerViewController.Configuration()
        fontConfig.includeFaces = true
        let fontPicker = UIFontPickerViewController(configuration: fontConfig)
        fontPicker.delegate = self
        self.present(fontPicker, animated: true, completion: nil)
    }
```

When your [`UIFontPickerViewControllerDelegate`](uifontpickerviewcontrollerdelegate.md) receives [`fontPickerViewControllerDidPickFont(_:)`](uifontpickerviewcontrollerdelegate/fontpickerviewcontrollerdidpickfont(_:).md), retrieve information about the user’s selected font from the font picker’s [`selectedFontDescriptor`](uifontpickerviewcontroller/selectedfontdescriptor.md).

## Topics

### Configuring a font picker to display in iOS
- [init(configuration: UIFontPickerViewController.Configuration)](uifontpickerviewcontroller/init(configuration:).md)
  Creates a controller for a font picker view.
- [var configuration: UIFontPickerViewController.Configuration](uifontpickerviewcontroller/configuration-swift.property.md)
  Settings for fonts the font picker should offer to the user and how to display those fonts.
- [UIFontPickerViewController.Configuration](uifontpickerviewcontroller/configuration-swift.class.md)
  The filters and display settings a font picker view controller uses to set up a font picker.
### Responding to font picker interactions
- [var delegate: (any UIFontPickerViewControllerDelegate)?](uifontpickerviewcontroller/delegate.md)
  The object that handles messages about the user’s interaction with a font picker.
- [protocol UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)
  A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [var selectedFontDescriptor: UIFontDescriptor?](uifontpickerviewcontroller/selectedfontdescriptor.md)
  Information about the font family or face selected by the user in the font picker.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [protocol UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)
  A set of optional methods for receiving messages about the user’s interaction with the font picker.
- [UIFontPickerViewController.Configuration](uifontpickerviewcontroller/configuration-swift.class.md)
  The filters and display settings a font picker view controller uses to set up a font picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontpickerviewcontroller)*