# supportedFamilies(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the sizes that a widget supports.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency func supportedFamilies(_ families: [WidgetFamily]) -> some WidgetConfiguration
```

#### Return Value

A widget configuration that supports the sizes you specify.

## Parameters

- `families`: The set of sizes the widget supports.

## See Also

- [func contentMarginsDisabled() -> some WidgetConfiguration](widgetconfiguration/contentmarginsdisabled.md)
  Disable default content margins.
- [func disfavoredLocations([WidgetLocation], for: [WidgetFamily]) -> some WidgetConfiguration](widgetconfiguration/disfavoredlocations(_:for:).md)
  Sets the disfavored locations for a widget.
- [func containerBackgroundRemovable(Bool) -> some WidgetConfiguration](widgetconfiguration/containerbackgroundremovable(_:).md)
  A modifier that marks the background of a widget as removable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedfamilies(_:))*