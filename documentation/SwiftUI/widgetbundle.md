# WidgetBundle

**Framework**: SwiftUI  
**Kind**: protocol

A container used to expose multiple widgets from a single widget extension.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol WidgetBundle
```

#### Overview

To support multiple types of widgets, add the `@main` attribute to a structure that conforms to `WidgetBundle`. For example, a game might have one widget to display summary information about the game and a second widget to display detailed information about individual characters.

```swift
@main
struct GameWidgets: WidgetBundle {
   var body: some Widget {
       GameStatusWidget()
       CharacterDetailWidget()
   }
}
```

## Topics

### Implementing a widget bundle
- [var body: Self.Body](widgetbundle/body-swift.property.md)
  Declares the group of widgets that an app supports.
- [associatedtype Body : Widget](widgetbundle/body-swift.associatedtype.md)
  The type of widget that represents the content of the bundle.
- [struct WidgetBundleBuilder](widgetbundlebuilder.md)
  A custom attribute that constructs a widget bundle’s body.
### Running a widget bundle
- [init()](widgetbundle/init.md)
  Creates a widget bundle using the bundle’s body as its content.
- [static func main()](widgetbundle/main.md)
  Initializes and runs the widget bundle.

## See Also

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
- [struct LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md)
  A type-erased widget configuration.
- [protocol WidgetConfiguration](widgetconfiguration.md)
  A type that describes a widget’s content.
- [struct EmptyWidgetConfiguration](emptywidgetconfiguration.md)
  An empty widget configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetbundle)*