# navigationSubtitle(_:)

**Framework**: FamilyControls  
**Kind**: method

Configures the view’s subtitle for purposes of navigation, using a string.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func navigationSubtitle<S>(_ subtitle: S) -> some View where S : StringProtocol
```

#### Discussion

A view’s navigation subtitle is used to provide additional contextual information alongside the navigation title. On macOS, the primary destination’s subtitle is displayed with the navigation title in the titlebar.

## Parameters

- `title`: The subtitle to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/navigationsubtitle(_:)-7gq2r)*