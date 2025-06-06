# Widget

**Framework**: SwiftUI  
**Kind**: protocol

The configuration and content of a widget to display on the Home screen or in Notification Center.

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
@preconcurrency protocol Widget
```

#### Overview

Widgets show glanceable and relevant content from your app right on the iOS Home screen or in Notification Center on macOS. Users can add, configure, and arrange widgets to suit their individual needs. You can provide multiple types of widgets, each presenting a specific kind of information. When users want more information, like to read the full article for a headline or to see the details of a package delivery, the widget lets them get to the information in your app quickly.

There are three key components to a widget:

- A configuration that determines whether the widget is configurable, identifies the widget, and defines the SwiftUI views that show the widget’s content.
- A timeline provider that drives the process of updating the widget’s view over time.
- SwiftUI views used by WidgetKit to display the widget.

For information about adding a widget extension to your app, and keeping your widget up to date, see [`Creating a widget extension`](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension) and [`Keeping a widget up to date`](https://developer.apple.com/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date), respectively.

By adding a custom SiriKit intent definition, you can let users customize their widgets to show the information that’s most relevant to them. If you’ve already added support for Siri or Shortcuts, you’re well on your way to supporting customizable widgets. For more information, see [`Making a configurable widget`](https://developer.apple.com/documentation/WidgetKit/Making-a-Configurable-Widget).

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Implementing a widget
- [var body: Self.Body](widget/body-swift.property.md)
  The content and behavior of the widget.
- [associatedtype Body : WidgetConfiguration](widget/body-swift.associatedtype.md)
  The type of configuration representing the content of the widget.
### Running a widget
- [init()](widget/init.md)
  Creates a widget using `body` as its content.
- [static func main()](widget/main.md)
  Initializes and runs the widget.

## See Also

- [Building Widgets Using WidgetKit and SwiftUI](../widgetkit/building_widgets_using_widgetkit_and_swiftui.md)
  Create widgets to show your app’s content on the Home screen, with custom intents for user-customizable settings.
- [Creating a widget extension](../WidgetKit/Creating-a-Widget-Extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Keeping a widget up to date](../WidgetKit/Keeping-a-Widget-Up-To-Date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [Making a configurable widget](../WidgetKit/Making-a-Configurable-Widget.md)
  Give people the option to customize their widgets by adding a custom app intent to your project.
- [protocol WidgetBundle](widgetbundle.md)
  A container used to expose multiple widgets from a single widget extension.
- [struct LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md)
  A type-erased widget configuration.
- [protocol WidgetConfiguration](widgetconfiguration.md)
  A type that describes a widget’s content.
- [struct EmptyWidgetConfiguration](emptywidgetconfiguration.md)
  An empty widget configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widget)*