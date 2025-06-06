# navigationSubtitle(_:)

**Framework**: MusicKit  
**Kind**: method

Configures the view’s subtitle for purposes of navigation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func navigationSubtitle(_ subtitle: Text) -> some View
```

#### Discussion

A view’s navigation subtitle is used to provide additional contextual information alongside the navigation title. On macOS, the primary destination’s subtitle is displayed with the navigation title in the titlebar.

## Parameters

- `subtitle`: The subtitle to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/navigationsubtitle(_:)-44y3k)*