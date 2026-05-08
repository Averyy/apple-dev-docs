# WidgetConfiguration

**Framework**: SwiftUI  
**Kind**: protocol

A type that describes a widget’s content.

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
@preconcurrency protocol WidgetConfiguration
```

#### Overview

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
- [var body: Self.Body](widgetconfiguration/body-swift.property.md)
  The content and behavior of this widget.
- [associatedtype Body : WidgetConfiguration](widgetconfiguration/body-swift.associatedtype.md)
  The type of widget configuration representing the body of this configuration.
### Setting a name
- [func configurationDisplayName(_:)](widgetconfiguration/configurationdisplayname(_:).md)
  Sets the localized name shown for a widget when a user adds or edits the widget.
### Setting a description
- [func description(_:)](widgetconfiguration/description(_:).md)
  Sets the description shown for a widget when a user adds or edits it using the contents of a text view.
### Setting the appearance
- [func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration](widgetconfiguration/supportedfamilies(_:).md)
  Sets the sizes that a widget supports.
- [func contentMarginsDisabled() -> some WidgetConfiguration](widgetconfiguration/contentmarginsdisabled.md)
  Disable default content margins.
- [func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some WidgetConfiguration](widgetconfiguration/disfavoredlocations(_:for:).md)
  Sets the disfavored locations for a widget.
- [func containerBackgroundRemovable(Bool) -> some WidgetConfiguration](widgetconfiguration/containerbackgroundremovable(_:).md)
  A modifier that marks the background of a widget as removable.
### Managing background tasks
- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some WidgetConfiguration](widgetconfiguration/backgroundtask(_:action:).md)
  Runs the given action when the system provides a background task.
- [func onBackgroundURLSessionEvents(matching:_:)](widgetconfiguration/onbackgroundurlsessionevents(matching:_:).md)
  Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.
### Instance Methods
- [func associatedKind(String?) -> some WidgetConfiguration](widgetconfiguration/associatedkind(_:).md)
  Tells the system that a relevance-based widget can replace a timeline-based widget.
- [func promptsForUserConfiguration() -> some WidgetConfiguration](widgetconfiguration/promptsforuserconfiguration.md)
  Specifies that a widget’s configuration UI should be automatically presented after the widget is added.
- [func pushHandler(any WidgetPushHandler.Type) -> some WidgetConfiguration](widgetconfiguration/pushhandler(_:).md)
  Register a type that can handle push tokens changing for widgets.
- [func supplementalActivityFamilies([ActivityFamily]) -> some WidgetConfiguration](widgetconfiguration/supplementalactivityfamilies(_:).md)
  Sets the sizes that a Live Activity supports.
- [func supportedMountingStyles([WidgetMountingStyle]) -> some WidgetConfiguration](widgetconfiguration/supportedmountingstyles(_:).md)
  Specifies the mounting style for this widget.
- [func widgetTexture(WidgetTexture) -> some WidgetConfiguration](widgetconfiguration/widgettexture(_:).md)
  Specifies the widget texture for this widget.

## Relationships

### Conforming Types
- [EmptyWidgetConfiguration](emptywidgetconfiguration.md)
- [LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md)

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
- [protocol WidgetBundle](widgetbundle.md)
  A container used to expose multiple widgets from a single widget extension.
- [struct LimitedAvailabilityConfiguration](limitedavailabilityconfiguration.md)
  A type-erased widget configuration.
- [struct EmptyWidgetConfiguration](emptywidgetconfiguration.md)
  An empty widget configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration)*