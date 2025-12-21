# pushHandler(_:)

**Framework**: SwiftUI  
**Kind**: method

Register a type that can handle push tokens changing for controls of this type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func pushHandler(_ pushHandlerType: any ControlPushHandler.Type) -> some ControlWidgetConfiguration
```

#### Overview

Use this to opt your control into using push notifications.

If you have multiple control types, you can choose to use the same push handler type for those control types.

When the push configuration of your controls changes, each handler type will be instantiated and [`pushTokensDidChange(controls:)`](https://developer.apple.com/documentation/WidgetKit/ControlPushHandler/pushTokensDidChange(controls:)) will be called.

## Parameters

- `pushHandlerType`: The type of the object that can handle push tokens you use to update the control with push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidgetconfiguration/pushhandler(_:))*