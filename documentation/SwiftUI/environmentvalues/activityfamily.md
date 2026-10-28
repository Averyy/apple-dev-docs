# activityFamily

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The size family of the current Live Activity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var activityFamily: ActivityFamily { get set }
```

## Discussion

A Live Activity you initiate on one device can also appear on a remote device that renders the Live Activity in a different family size. As a result, it renders for a specific family, depending on both the device and the location in which it appears. For example, when rendering on the iOS or iPadOS Lock Screen, the current family is https://developer.apple.com/documentation/WidgetKit/ActivityFamily/medium.

Use [`supplementalActivityFamilies(_:)`](../widgetconfiguration/supplementalactivityfamilies%28_%29.md) to opt in and allow your Live Activity to render with additional families.

## See Also

### Configuring a Live Activity
- [func activitySystemActionForegroundColor(Color?) -> some View](../view/activitysystemactionforegroundcolor%28_%29.md)
  The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [func activityBackgroundTint(Color?) -> some View](../view/activitybackgroundtint%28_%29.md)
  Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [var isActivityFullscreen: Bool](./isactivityfullscreen.md)
  A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/activityfamily)*