# Controls and indicators

**Framework**: SwiftUI

Display values and get user selections.

#### Overview

SwiftUI provides controls that enable user interaction specific to each platform and context. For example, people can initiate events with buttons and links, or choose among a set of discrete values with different kinds of pickers. You can also display information to the user with indicators like progress views and gauges.

![None](https://docs-assets.developer.apple.com/published/3d1d4d9ddf1ec58056b340ea15756488/controls-and-indicators-hero%402x.png)

Use these built-in controls and indicators when composing custom views, and style them to match the needs of your app’s user interface. For design guidance, see [`Menus and actions`](https://developer.apple.com/design/Human-Interface-Guidelines/menus-and-actions), [`Selection and input`](https://developer.apple.com/design/Human-Interface-Guidelines/selection-and-input), and [`Status`](https://developer.apple.com/design/Human-Interface-Guidelines/status) in the Human Interface Guidelines.

## Topics

### Creating buttons
- [struct Button](button.md)
  A control that initiates an action.
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonBorderShape(ButtonBorderShape) -> some View](view/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](view/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [var buttonRepeatBehavior: ButtonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md)
  Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [struct ButtonBorderShape](buttonbordershape.md)
  A shape used to draw a button’s border.
- [struct ButtonRole](buttonrole.md)
  A value that describes the purpose of a button.
- [struct ButtonRepeatBehavior](buttonrepeatbehavior.md)
  The options for controlling the repeatability of button actions.
- [struct ButtonSizing](buttonsizing.md)
### Creating special-purpose buttons
- [struct EditButton](editbutton.md)
  A button that toggles the edit mode environment value.
- [struct PasteButton](pastebutton.md)
  A system button that reads items from the pasteboard and delivers it to a closure.
- [struct RenameButton](renamebutton.md)
  A button that triggers a standard rename action.
### Linking to other content
- [struct Link](link.md)
  A control for navigating to a URL.
- [struct ShareLink](sharelink.md)
  A view that controls a sharing presentation.
- [struct SharePreview](sharepreview.md)
  A representation of a type to display in a share preview.
- [struct TextFieldLink](textfieldlink.md)
  A control that requests text input from the user when pressed.
- [struct HelpLink](helplink.md)
  A button with a standard appearance that opens app-specific help documentation.
### Getting numeric inputs
- [struct Slider](slider.md)
  A control for selecting a value from a bounded linear range of values.
- [struct Stepper](stepper.md)
  A control that performs increment and decrement actions.
- [struct Toggle](toggle.md)
  A control that toggles between on and off states.
- [func toggleStyle<S>(S) -> some View](view/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
### Choosing from a set of options
- [struct Picker](picker.md)
  A control for selecting from a set of mutually exclusive values.
- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func horizontalRadioGroupLayout() -> some View](view/horizontalradiogrouplayout.md)
  Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [func defaultWheelPickerItemHeight(CGFloat) -> some View](view/defaultwheelpickeritemheight(_:).md)
  Sets the default wheel-style picker item height.
- [var defaultWheelPickerItemHeight: CGFloat](environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [func paletteSelectionEffect(PaletteSelectionEffect) -> some View](view/paletteselectioneffect(_:).md)
  Specifies the selection effect to apply to a palette item.
- [struct PaletteSelectionEffect](paletteselectioneffect.md)
  The selection effect to apply to a palette item.
### Choosing dates
- [struct DatePicker](datepicker.md)
  A control for selecting an absolute date.
- [func datePickerStyle<S>(S) -> some View](view/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [struct MultiDatePicker](multidatepicker.md)
  A control for picking multiple dates.
- [var calendar: Calendar](environmentvalues/calendar.md)
  The current calendar that views should use when handling dates.
- [var timeZone: TimeZone](environmentvalues/timezone.md)
  The current time zone that views should use when handling dates.
### Choosing a color
- [struct ColorPicker](colorpicker.md)
  A control used to select a color from the system color picker UI.
### Indicating a value
- [struct Gauge](gauge.md)
  A view that shows a value within a range.
- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [struct ProgressView](progressview.md)
  A view that shows the progress toward completion of a task.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [struct DefaultDateProgressLabel](defaultdateprogresslabel.md)
  The default type of the current value label when used by a date-relative progress view.
- [struct DefaultButtonLabel](defaultbuttonlabel.md)
  The default label to use for a button.
### Indicating missing content
- [struct ContentUnavailableView](contentunavailableview.md)
  An interface, consisting of a label and additional content, that you display when the content of your app is unavailable to users.
### Providing haptic feedback
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T) -> some View](view/sensoryfeedback(_:trigger:).md)
  Plays the specified `feedback` when the provided `trigger` value changes.
- [func sensoryFeedback(trigger:_:)](view/sensoryfeedback(trigger:_:).md)
  Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [func sensoryFeedback<T>(SensoryFeedback, trigger: T, condition: (T, T) -> Bool) -> some View](view/sensoryfeedback(_:trigger:condition:).md)
  Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.
- [struct SensoryFeedback](sensoryfeedback.md)
  Represents a type of haptic and/or audio feedback that can be played.
### Sizing controls
- [func controlSize(_:)](view/controlsize(_:).md)
  Sets the size for controls within this view.
- [enum ControlSize](controlsize.md)
  The size classes, like regular or small, that you can apply to controls within a view.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controls-and-indicators)*