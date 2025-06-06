# UIColorPickerViewController

**Framework**: UIKit  
**Kind**: class

A view controller that manages the interface for selecting a color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIColorPickerViewController
```

#### Overview

[`UIColorPickerViewController`](uicolorpickerviewcontroller.md) provides a standard interface to select colors. Use this class instead of [`UIColorWell`](uicolorwell.md) if you need more fine-grained control over the presentation.

![Screenshot of a color picker in a popover presentation style, showing a spectrum of color options. The title of the color picker is Colors.](https://docs-assets.developer.apple.com/published/7a8215c6fe7d69222d5d869b01ef7f46/media-4195196%402x.png)

You typically present a [`UIColorPickerViewController`](uicolorpickerviewcontroller.md) as a popover:

```swift
// This example code appears in a subclass of UIViewController that conforms to
// UIColorPickerViewControllerDelegate.
func presentColorPicker() {
    let colorPicker = UIColorPickerViewController()
    colorPicker.title = "Background Color"
    colorPicker.supportsAlpha = false
    colorPicker.delegate = self
    colorPicker.modalPresentationStyle = .popover
    colorPicker.popoverPresentationController?.sourceItem = self.navigationItem.rightBarButtonItem
    self.present(colorPicker, animated: true)
}
```

You can also react to the color-selection change or the dismissal of the color picker by implementing the [`UIColorPickerViewControllerDelegate`](uicolorpickerviewcontrollerdelegate.md) functions.

## Topics

### Creating a color picker view controller
- [init()](uicolorpickerviewcontroller/init.md)
  Creates a color picker view controller.
### Configuring the color picker view controller
- [var delegate: (any UIColorPickerViewControllerDelegate)?](uicolorpickerviewcontroller/delegate.md)
  The delegate that receives updates about the color selection.
- [protocol UIColorPickerViewControllerDelegate](uicolorpickerviewcontrollerdelegate.md)
  The delegate protocol to inform about changes in color selection.
- [var selectedColor: UIColor](uicolorpickerviewcontroller/selectedcolor.md)
  The color selected by the user.
- [var supportsAlpha: Bool](uicolorpickerviewcontroller/supportsalpha.md)
  A Boolean value that enables alpha value control.

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

- [protocol UIColorPickerViewControllerDelegate](uicolorpickerviewcontrollerdelegate.md)
  The delegate protocol to inform about changes in color selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller)*