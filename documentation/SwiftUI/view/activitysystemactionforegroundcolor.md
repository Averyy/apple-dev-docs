# activitySystemActionForegroundColor(_:)

**Framework**: SwiftUI  
**Kind**: method

The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
@MainActor
@preconcurrency func activitySystemActionForegroundColor(_ color: Color?) -> some View
```

## Parameters

- `color`: The text color to use. Pass   to use the system’s default color.

## See Also

- [func activityBackgroundTint(Color?) -> some View](view/activitybackgroundtint(_:).md)
  Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [var isActivityFullscreen: Bool](environmentvalues/isactivityfullscreen.md)
  A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [var activityFamily: ActivityFamily](environmentvalues/activityfamily.md)
  The size family of the current Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/activitysystemactionforegroundcolor(_:))*