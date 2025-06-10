# navigationSubtitle(_:)

**Framework**: App Intents  
**Kind**: method

Configures the view’s subtitle for purposes of navigation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func navigationSubtitle(_ subtitle: Text) -> some View
```

#### Discussion

A view’s navigation subtitle is used to provide additional contextual information alongside the navigation title. On macOS, the primary destination’s subtitle is displayed with the navigation title in the titlebar. On iOS and iPadOS, the subtitle is displayed with the navigation title in the navigation bar.

## Parameters

- `subtitle`: The subtitle to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/navigationsubtitle(_:)-4r25d)*