# activityBackgroundTint(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Sets the tint color for the background of a Live Activity that appears on the Lock Screen.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
@preconcurrency func activityBackgroundTint(_ color: Color?) -> some View
```

#### Discussion

When you set a custom background tint color, consider setting a custom text color for the auxiliary button people use to end a Live Activity on the Lock Screen. To set a custom text color, use the [`activitySystemActionForegroundColor(_:)`](https://developer.apple.com/documentation/SwiftUI/View/activitySystemActionForegroundColor(_:)) view modifier.

## Parameters

- `color`: The background tint color to apply. To use the system’s default background material,   pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/activitybackgroundtint(_:))*