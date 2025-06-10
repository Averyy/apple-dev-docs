# disfavoredLocations(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Sets the disfavored locations for a widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func disfavoredLocations(_ locations: [WidgetLocation], for families: [WidgetFamily]) -> some WidgetConfiguration
```

#### Discussion

A widget can appear in different contexts on different platforms. For example, a small system widget appears by default on the Home Screen and in Today View on iPhone, on the iPad Lock Screen, and so on. This gives more people opportunity to view data and functionality that your widget provides. However, some widgets may not work well in a location. For example, a widget that heavily relies on high-resolution photos and background colors for its functionality may not work well on the Lock Screen, where the system applies a vibrant treatment to the widget. To tell the system that the widget gallery should show a widget in the “Other” section of the widget gallery for a specific context, use the `.disfavoredLocations` modifier.

The following code snippet tells the system to show the small system family widget in the “Other” section of the widget gallery for the disfavored `WidgetLocation/lockScreen` and `WidgetLocation/homeScreen` locations.

```swift
lockScreenOnlyConfig
    .disfavoredLocations([.lockScreen, .homeScreen], for: [.systemSmall])
```

You can use subsequent calls to `disfavoredLocations(_:families:)` to join them and set disfavored locations for different families:

```swift
widgetConfig
    .disfavoredLocations([.lockScreen, .homeScreen], for: [.systemSmall])
    .disfavoredLocations([.homescreen], for: [.systemMedium])
```

## Parameters

- `locations`: An array of disfavored locations for a widget.
- `families`: The families you want to mark as disfavored in the given locations.

## See Also

- [func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration](widgetconfiguration/supportedfamilies(_:).md)
  Sets the sizes that a widget supports.
- [func contentMarginsDisabled() -> some WidgetConfiguration](widgetconfiguration/contentmarginsdisabled.md)
  Disable default content margins.
- [func containerBackgroundRemovable(Bool) -> some WidgetConfiguration](widgetconfiguration/containerbackgroundremovable(_:).md)
  A modifier that marks the background of a widget as removable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/disfavoredlocations(_:for:))*