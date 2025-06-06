# NSComboButton

**Framework**: AppKit  
**Kind**: class

A button with a pull-down menu and a default action.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
class NSComboButton
```

#### Overview

An [`NSComboButton`](nscombobutton.md) object is a button that displays a title string, image, and an optional control for displaying a menu. Use this control in places where you want to offer a button with a default action and one or more alternative actions. Clicking the title or image executes the default action you provide, and clicking the menu control displays a menu for selecting a different action. If you configure the button to hide the menu control, a long-press gesture displays the menu.

After you create a combo button programmatically or in Interface Builder, choose the button [`style`](nscombobutton/style-swift.property.md) you want and add a title or image for your content. A combo button has a default action, which you specify at creation time. You can also change that action later using the inherited [`target`](nscontrol/target.md) and [`action`](nscontrol/action.md) properties. To specify one or more alternative actions, configure a menu with those actions and assign it to the button’s [`menu`](nscombobutton/menu.md) property.

This control doesn’t use an [`NSCell`](nscell.md) object for its underlying implementation. It also doesn’t support the addition of a contextual menu.

## Topics

### Creating a Combo Button
- [convenience init(title: String, image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)](nscombobutton/init(title:image:menu:target:action:).md)
  Creates a combo button that displays both a title and image.
- [convenience init(title: String, menu: NSMenu?, target: Any?, action: Selector?)](nscombobutton/init(title:menu:target:action:).md)
  Creates a combo button that displays a title.
- [convenience init(image: NSImage, menu: NSMenu?, target: Any?, action: Selector?)](nscombobutton/init(image:menu:target:action:).md)
  Creates a combo button that displays an image.
### Configuring the Button Appearance
- [var style: NSComboButton.Style](nscombobutton/style-swift.property.md)
  The appearance setting that determines how the button presents its menu .
- [NSComboButton.Style](nscombobutton/style-swift.enum.md)
  Constants that indicate how a combo button presents its menu.
- [var title: String](nscombobutton/title.md)
  The localized string that the button displays.
- [var image: NSImage?](nscombobutton/image.md)
  The image that the button displays.
- [var imageScaling: NSImageScaling](nscombobutton/imagescaling.md)
  The scaling behavior to apply to the button’s image.
### Specifying the Alternative Actions
- [var menu: NSMenu](nscombobutton/menu.md)
  The menu that contains the button’s alternate actions.

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [Date Picker](date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSProgressIndicator](nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSRuleEditor](nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.
- [Slider](slider.md)
  Display a range of values from which the user selects a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobutton)*