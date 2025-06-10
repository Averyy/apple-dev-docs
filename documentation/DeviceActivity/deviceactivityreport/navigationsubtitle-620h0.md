# navigationSubtitle(_:)

**Framework**: DeviceActivity  
**Kind**: method

Configures the view’s subtitle for purposes of navigation, using a localized string resource.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func navigationSubtitle(_ subtitleKey: LocalizedStringResource) -> some View
```

#### Discussion

A view’s navigation subtitle is used to provide additional contextual information alongside the navigation title. On macOS, the primary destination’s subtitle is displayed with the navigation title in the titlebar. On iOS and iPadOS, the subtitle is displayed with the navigation title in the navigation bar.

## Parameters

- `subtitleResource`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/navigationsubtitle(_:)-620h0)*