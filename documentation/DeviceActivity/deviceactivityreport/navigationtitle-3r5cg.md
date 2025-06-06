# navigationTitle(_:)

**Framework**: DeviceActivity  
**Kind**: method

Configures the view’s title for purposes of navigation, using a custom view.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
nonisolated
func navigationTitle<V>(@ViewBuilder _ title: () -> V) -> some View where V : View
```

#### Discussion

A view’s navigation title is used to visually display the current navigation state of an interface. On iOS and watchOS, when a view is navigated to inside of a navigation view, that view’s title is displayed in the navigation bar. On iPadOS, the primary destination’s navigation title is reflected as the window’s title in the App Switcher. Similarly on macOS, the primary destination’s title is used as the window title in the titlebar, Windows menu and Mission Control.

## Parameters

- `title`: The view to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/navigationtitle(_:)-3r5cg)*