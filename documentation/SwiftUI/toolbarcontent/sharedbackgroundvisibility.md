# sharedBackgroundVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
nonisolated
func sharedBackgroundVisibility(_ visibility: Visibility) -> some ToolbarContent
```

#### Discussion

This modifier adjusts the visibility of that effect. Hiding the effect will cause the item to be placed in its own grouping.

```swift
ContentView()
    .toolbar {
        ToolbarItem(placement: principal) {
            BuildStatus()
        }
        .sharedBackgroundVisibility(.hidden)
    }
```

## Parameters

- `visibility`: The visibility of the background effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontent/sharedbackgroundvisibility(_:))*