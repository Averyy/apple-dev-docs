# pushHandler(_:)

**Framework**: SwiftUI  
**Kind**: method

Register a type that can handle push tokens changing for widgets.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func pushHandler(_ pushHandlerType: any WidgetPushHandler.Type) -> some WidgetConfiguration
```

#### Overview

Use this to opt this widget into supporting updates via push notifications.

If you have multiple widget configurations, you can choose to use the same push handler type for those widget configurations.

When the push configuration of your widgets changes, each unique handler type will be instantiated and [`pushTokenDidChange(_:widgets:)`](https://developer.apple.com/documentation/WidgetKit/WidgetPushHandler/pushTokenDidChange(_:widgets:)) will be called.

## Parameters

- `pushHandlerType`: The type of the object that can handle push tokens you use to update the widget with push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/pushhandler(_:))*