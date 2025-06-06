# isActivityFullscreen

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+

## Declaration

```swift
@backDeployed(before: iOS 17.0)
var isActivityFullscreen: Bool { get }
```

#### Discussion

When a Live Activity fills the entire screen, the system extends the background tint color you set with the [`activityBackgroundTint(_:)`](View/activityBackgroundTint(_:).md) modifier to fill the screen.

Note that this environment variable is always `false` in iOS 16.

## See Also

- [func activitySystemActionForegroundColor(Color?) -> some View](view/activitysystemactionforegroundcolor(_:).md)
  The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [func activityBackgroundTint(Color?) -> some View](view/activitybackgroundtint(_:).md)
  Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [var activityFamily: ActivityFamily](environmentvalues/activityfamily.md)
  The size family of the current Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isactivityfullscreen)*