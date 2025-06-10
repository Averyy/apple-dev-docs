# activityBackgroundTint(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the tint color for the background of a Live Activity that appears on the Lock Screen.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
@MainActor
@preconcurrency func activityBackgroundTint(_ color: Color?) -> some View
```

#### Discussion

When you set a custom background tint color, consider setting a custom text color for the auxiliary button people use to end a Live Activity on the Lock Screen. To set a custom text color, use the [`activitySystemActionForegroundColor(_:)`](View/activitySystemActionForegroundColor(_:).md) view modifier.

## Parameters

- `color`: The background tint color to apply. To use the system’s default background material,   pass  .

## See Also

- [func activitySystemActionForegroundColor(Color?) -> some View](view/activitysystemactionforegroundcolor(_:).md)
  The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [var isActivityFullscreen: Bool](environmentvalues/isactivityfullscreen.md)
  A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [var activityFamily: ActivityFamily](environmentvalues/activityfamily.md)
  The size family of the current Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/activitybackgroundtint(_:))*