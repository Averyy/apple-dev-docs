# View styles

**Framework**: SwiftUI

Apply built-in and custom appearances and behaviors to different types of views.

#### Overview

SwiftUI defines built-in styles for certain kinds of views and automatically selects the appropriate style for a particular presentation context. For example, a [`Label`](label.md) might appear as an icon, a string title, or both, depending on factors like the platform, whether the view appears in a toolbar, and so on.

![None](https://docs-assets.developer.apple.com/published/7ba769e017aa157b1b47692780e74e9a/view-styles-hero%402x.png)

You can override the automatic style by using one of the style view modifiers. These modifiers typically propagate throughout a container view, so that you can wrap a view hierarchy in a style modifier to affect all the views of the given type within the hierarchy.

Any of the style protocols that define a `makeBody(configuration:)` method, like [`ToggleStyle`](togglestyle.md), also enable you to define custom styles. Create a type that conforms to the corresponding style protocol and implement its `makeBody(configuration:)` method. Then apply the new style using a style view modifier exactly like a built-in style.

## Topics

### Styling buttons
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [protocol ButtonStyle](buttonstyle.md)
  A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [struct ButtonStyleConfiguration](buttonstyleconfiguration.md)
  The properties of a button.
- [protocol PrimitiveButtonStyle](primitivebuttonstyle.md)
  A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [struct PrimitiveButtonStyleConfiguration](primitivebuttonstyleconfiguration.md)
  The properties of a button.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
### Styling pickers
- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [protocol PickerStyle](pickerstyle.md)
  A type that specifies the appearance and interaction of all pickers within a view hierarchy.
- [func datePickerStyle<S>(S) -> some View](view/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [protocol DatePickerStyle](datepickerstyle.md)
  A type that specifies the appearance and interaction of all date pickers within a view hierarchy.
### Styling menus
- [func menuStyle<S>(S) -> some View](view/menustyle(_:).md)
  Sets the style for menus within this view.
- [protocol MenuStyle](menustyle.md)
  A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.
- [struct MenuStyleConfiguration](menustyleconfiguration.md)
  A configuration of a menu.
### Styling toggles
- [func toggleStyle<S>(S) -> some View](view/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [protocol ToggleStyle](togglestyle.md)
  The appearance and behavior of a toggle.
- [struct ToggleStyleConfiguration](togglestyleconfiguration.md)
  The properties of a toggle instance.
### Styling indicators
- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [protocol GaugeStyle](gaugestyle.md)
  Defines the implementation of all gauge instances within a view hierarchy.
- [struct GaugeStyleConfiguration](gaugestyleconfiguration.md)
  The properties of a gauge instance.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [protocol ProgressViewStyle](progressviewstyle.md)
  A type that applies standard interaction behavior to all progress views within a view hierarchy.
- [struct ProgressViewStyleConfiguration](progressviewstyleconfiguration.md)
  The properties of a progress view instance.
### Styling views that display text
- [func labelStyle<S>(S) -> some View](view/labelstyle(_:).md)
  Sets the style for labels within this view.
- [protocol LabelStyle](labelstyle.md)
  A type that applies a custom appearance to all labels within a view.
- [struct LabelStyleConfiguration](labelstyleconfiguration.md)
  The properties of a label.
- [func textFieldStyle<S>(S) -> some View](view/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [protocol TextFieldStyle](textfieldstyle.md)
  A specification for the appearance and interaction of a text field.
- [func textEditorStyle(some TextEditorStyle) -> some View](view/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [protocol TextEditorStyle](texteditorstyle.md)
  A specification for the appearance and interaction of a text editor.
- [struct TextEditorStyleConfiguration](texteditorstyleconfiguration.md)
  The properties of a text editor.
### Styling collection views
- [func listStyle<S>(S) -> some View](view/liststyle(_:).md)
  Sets the style for lists within this view.
- [protocol ListStyle](liststyle.md)
  A protocol that describes the behavior and appearance of a list.
- [func tableStyle<S>(S) -> some View](view/tablestyle(_:).md)
  Sets the style for tables within this view.
- [protocol TableStyle](tablestyle.md)
  A type that applies a custom appearance to all tables within a view.
- [struct TableStyleConfiguration](tablestyleconfiguration.md)
  The properties of a table.
- [func disclosureGroupStyle<S>(S) -> some View](view/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [protocol DisclosureGroupStyle](disclosuregroupstyle.md)
  A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.
### Styling navigation views
- [func navigationSplitViewStyle<S>(S) -> some View](view/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [protocol NavigationSplitViewStyle](navigationsplitviewstyle.md)
  A type that specifies the appearance and interaction of navigation split views within a view hierarchy.
- [func tabViewStyle<S>(S) -> some View](view/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [protocol TabViewStyle](tabviewstyle.md)
  A specification for the appearance and interaction of a tab view.
### Styling groups
- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [protocol ControlGroupStyle](controlgroupstyle.md)
  Defines the implementation of all control groups within a view hierarchy.
- [struct ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md)
  The properties of a control group.
- [func formStyle<S>(S) -> some View](view/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [protocol FormStyle](formstyle.md)
  The appearance and behavior of a form.
- [struct FormStyleConfiguration](formstyleconfiguration.md)
  The properties of a form instance.
- [func groupBoxStyle<S>(S) -> some View](view/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [protocol GroupBoxStyle](groupboxstyle.md)
  A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [struct GroupBoxStyleConfiguration](groupboxstyleconfiguration.md)
  The properties of a group box instance.
- [func indexViewStyle<S>(S) -> some View](view/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [protocol IndexViewStyle](indexviewstyle.md)
  Defines the implementation of all `IndexView` instances within a view hierarchy.
- [func labeledContentStyle<S>(S) -> some View](view/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [protocol LabeledContentStyle](labeledcontentstyle.md)
  The appearance and behavior of a labeled content instance..
- [struct LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md)
  The properties of a labeled content instance.
### Styling windows from a view inside the window
- [func presentedWindowStyle<S>(S) -> some View](view/presentedwindowstyle(_:).md)
  Sets the style for windows created by interacting with this view.
- [func presentedWindowToolbarStyle<S>(S) -> some View](view/presentedwindowtoolbarstyle(_:).md)
  Sets the style for the toolbar in windows created by interacting with this view.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Menus and commands](menus-and-commands.md)
  Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-styles)*