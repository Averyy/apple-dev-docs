# navigationSubtitle(_:)

**Framework**: FamilyControls  
**Kind**: method

Configures the view’s subtitle for purposes of navigation, using a localized string.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func navigationSubtitle(_ subtitleKey: LocalizedStringKey) -> some View
```

#### Discussion

A view’s navigation subtitle is used to provide additional contextual information alongside the navigation title. On macOS, the primary destination’s subtitle is displayed with the navigation title in the titlebar.

## Parameters

- `subtitleKey`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/navigationsubtitle(_:)-479i0)*