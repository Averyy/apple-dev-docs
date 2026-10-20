# CLKComplicationPrivacyBehavior.hideOnLockScreen

**Framework**: ClockKit  
**Kind**: case  
**Role**: Case

Don’t show the complication data when the Apple Watch is locked.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
case hideOnLockScreen
```

```c
CLKComplicationPrivacyBehaviorHideOnLockScreen
```

#### Discussion

For circular, modular small, and utilitarian small complications, ClockKit displays the complication icon provided by your WatchKit extension. For modular large, and utilitarian large templates, ClockKit displays your app name.

## See Also

### Constants
- [CLKComplicationPrivacyBehavior.showOnLockScreen](./showonlockscreen.md)
  Show the complication data when the Apple Watch is locked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationprivacybehavior/hideonlockscreen)*