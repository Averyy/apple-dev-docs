# Style modifiers

**Framework**: SwiftUI

Apply built-in styles to different types of views.

#### Overview

SwiftUI defines built-in styles for certain kinds of views, and chooses the appropriate style for a particular presentation context. For example, a [`Label`](label.md) might appear as an icon, a string title, or both, depending on factors like the platform, whether the view appears in a toolbar, and so on.

You can override the automatic style by using one of the style modifiers. These modifiers typically propagate through container views, so you can wrap an entire view hierarchy in a style modifier to affect all the views of the given type within the hierarchy. Some view types enable you to create custom styles, which you also apply using style modifiers.

For more information about styling views, see [`View styles`](view-styles.md).

## Topics

### Controls
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func datePickerStyle<S>(S) -> some View](view/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func menuStyle<S>(S) -> some View](view/menustyle(_:).md)
  Sets the style for menus within this view.
- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func toggleStyle<S>(S) -> some View](view/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
### Indicators
- [func gaugeStyle<S>(S) -> some View](view/gaugestyle(_:).md)
  Sets the style for gauges within this view.
- [func progressViewStyle<S>(S) -> some View](view/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
### Text
- [func labelStyle<S>(S) -> some View](view/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func textFieldStyle<S>(S) -> some View](view/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func textEditorStyle(some TextEditorStyle) -> some View](view/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
### Collections
- [func listStyle<S>(S) -> some View](view/liststyle(_:).md)
  Sets the style for lists within this view.
- [func tableStyle<S>(S) -> some View](view/tablestyle(_:).md)
  Sets the style for tables within this view.
- [func disclosureGroupStyle<S>(S) -> some View](view/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
### Presentation
- [func navigationSplitViewStyle<S>(S) -> some View](view/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func tabViewStyle<S>(S) -> some View](view/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
- [func presentedWindowStyle<S>(S) -> some View](view/presentedwindowstyle(_:).md)
  Sets the style for windows created by interacting with this view.
- [func presentedWindowToolbarStyle<S>(S) -> some View](view/presentedwindowtoolbarstyle(_:).md)
  Sets the style for the toolbar in windows created by interacting with this view.
### Groups
- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func groupBoxStyle<S>(S) -> some View](view/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func indexViewStyle<S>(S) -> some View](view/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.

## See Also

- [Layout modifiers](view-layout.md)
  Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.
- [Graphics and rendering modifiers](view-graphics-and-rendering.md)
  Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-style-modifiers)*