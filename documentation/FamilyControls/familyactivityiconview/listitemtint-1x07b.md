# listItemTint(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the tint effect for content in a list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func listItemTint(_ tint: ListItemTint?) -> some View
```

#### Discussion

The containing list’s style applies the tint as appropriate. For example, watchOS uses the tint color for its background platter appearance. Sidebars on iOS and macOS apply the tint color to their `Label` icons, which otherwise use the accent color by default.

## Parameters

- `tint`: The tint effect to use. Use   to avoid  overriding   the inherited tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/listitemtint(_:)-1x07b)*