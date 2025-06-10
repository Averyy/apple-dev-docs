# UIColorWell

**Framework**: UIKit  
**Kind**: class

A control that displays a color picker.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIColorWell
```

## Topics

### Configuring color picker attributes
- [var title: String?](uicolorwell/title.md)
  The title for the color picker.
- [var maximumLinearExposure: CGFloat](uicolorwell/maximumlinearexposure.md)
  The maximum exposure to apply to a color when returned by the color well.
- [var supportsAlpha: Bool](uicolorwell/supportsalpha.md)
  A Boolean value that determines whether the color picker supports alpha values.
- [var supportsEyedropper: Bool](uicolorwell/supportseyedropper.md)
  If set to `NO` the eyedropper functionality is not supported for this color well.
- [var selectedColor: UIColor?](uicolorwell/selectedcolor.md)
  The selected color in the color picker.

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class UIControl](uicontrol.md)
  The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
- [class UIButton](uibutton.md)
  A control that executes your custom code in response to user interactions.
- [class UIDatePicker](uidatepicker.md)
  A control for inputting date and time values.
- [class UIPageControl](uipagecontrol.md)
  A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.
- [class UISegmentedControl](uisegmentedcontrol.md)
  A horizontal control that consists of multiple segments, each segment functioning as a discrete button.
- [class UISlider](uislider.md)
  A control for selecting a single value from a continuous range of values.
- [class UIStepper](uistepper.md)
  A control for incrementing or decrementing a value.
- [class UISwitch](uiswitch.md)
  A control that offers a binary choice, such as on/off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolorwell)*