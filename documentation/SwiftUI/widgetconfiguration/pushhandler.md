# pushHandler(_:)

**Framework**: SwiftUI  
**Kind**: method

Register a type that can handle push tokens changing for widgets.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func pushHandler(_ pushHandlerType: any WidgetPushHandler.Type) -> some WidgetConfiguration
```

#### Discussion

Use this to opt this widget into supporting updates via push notifications.

If you have multiple widget configurations, you can choose to use the same push handler type for those widget configurations.

When the push configuration of your widgets changes, each unique handler type will be instantiated and `WidgetPushHandler/pushTokenDidChange(_:)` will be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/widgetconfiguration/pushhandler(_:))*