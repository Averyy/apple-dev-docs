# App extensions

**Framework**: SwiftUI

Extend your app’s basic functionality to other parts of the system, like by adding a Widget.

#### Overview

Use SwiftUI along with [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit) to add widgets to your app.

![None](https://docs-assets.developer.apple.com/published/b4da7f7032a035f40f8426797d9c227c/app-extensions-hero%402x.png)

Widgets provide quick access to relevant content from your app. Define a structure that conforms to the [`Widget`](widget.md) protocol, and declare a view hierarchy for the widget. Configure the views inside the widget as you do other SwiftUI views, using view modifiers, including a few widget-specific modifiers.

For design guidance, see [`Widgets`](https://developer.apple.com/design/Human-Interface-Guidelines/widgets) in the Human Interface Guidelines.

## Topics

### Creating widgets
- [Building Widgets Using WidgetKit and SwiftUI](../widgetkit/building_widgets_using_widgetkit_and_swiftui.md)
  Create widgets to show your app’s content on the Home screen, with custom intents for user-customizable settings.
- [Creating a widget extension](../WidgetKit/Creating-a-Widget-Extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](../WidgetKit/Keeping-a-Widget-Up-To-Date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Making a configurable widget](../WidgetKit/Making-a-Configurable-Widget.md)
  Give people the option to customize their widgets by adding a custom app intent to your project.
- [protocol Widget](widget.md)
  The configuration and content of a widget to display on the Home screen or in Notification Center.
- [protocol WidgetBundle](widgetbundle.md)
  A container used to expose multiple widgets from a single widget extension.
- [struct LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md)
  A type-erased widget configuration.
- [protocol WidgetConfiguration](widgetconfiguration.md)
  A type that describes a widget’s content.
- [struct EmptyWidgetConfiguration](emptywidgetconfiguration.md)
  An empty widget configuration.
### Composing control widgets
- [protocol ControlWidget](controlwidget.md)
  The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [protocol ControlWidgetConfiguration](controlwidgetconfiguration.md)
  A type that describes a control widget’s content.
- [struct EmptyControlWidgetConfiguration](emptycontrolwidgetconfiguration.md)
  An empty control widget configuration.
- [struct ControlWidgetConfigurationBuilder](controlwidgetconfigurationbuilder.md)
  A custom attribute that constructs a control widget’s body.
- [protocol ControlWidgetTemplate](controlwidgettemplate.md)
  A type that describes a control widget’s content.
- [struct EmptyControlWidgetTemplate](emptycontrolwidgettemplate.md)
  An empty control widget template.
- [struct ControlWidgetTemplateBuilder](controlwidgettemplatebuilder.md)
  A custom attribute that constructs a control widget template’s body.
- [func controlWidgetActionHint(_:)](view/controlwidgetactionhint(_:).md)
  The action hint of the control described by the modified label.
- [func controlWidgetStatus(_:)](view/controlwidgetstatus(_:).md)
  The status of the control described by the modified label.
### Labeling a widget
- [func widgetLabel(_:)](view/widgetlabel(_:).md)
  Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.
- [func widgetLabel<Label>(label: () -> Label) -> some View](view/widgetlabel(label:).md)
  Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
### Styling a widget group
- [func accessoryWidgetGroupStyle(AccessoryWidgetGroupStyle) -> some View](view/accessorywidgetgroupstyle(_:).md)
  The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.
### Controlling the accented group
- [func widgetAccentable(Bool) -> some View](view/widgetaccentable(_:).md)
  Adds the view and all of its subviews to the accented group.
### Managing placement in the Dynamic Island
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View](view/dynamicisland(verticalplacement:).md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.

## See Also

- [App organization](app-organization.md)
  Define the entry point and top-level structure of your app.
- [Scenes](scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](documents.md)
  Enable people to open and manage documents.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](search.md)
  Enable people to search for text or other content within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/app-extensions)*