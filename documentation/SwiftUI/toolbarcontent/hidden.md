# hidden(_:)

**Framework**: SwiftUI  
**Kind**: method

Hides a toolbar item within its toolbar.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 15.0+
- tvOS 27.2+ (Beta)
- visionOS 26.4+
- watchOS 27.2+ (Beta)

## Declaration

```swift
nonisolated
func hidden(_ hidden: Bool = true) -> some ToolbarContent
```

#### Discussion

Use this modifier to conditionally display a toolbar item in the toolbar.

```swift
struct ContentView {
    @State private var showDownloads = false

    var body: some View {
        BrowserView()
            .toolbar {
                ToolbarItem {
                    DownloadsButton()
                }
                .hidden(!showDownloads)
            }
    }
}
```

## Parameters

- `hidden`: Whether the toolbar item is hidden.

## See Also

- [func sharedBackgroundVisibility(Visibility) -> some ToolbarContent](toolbarcontent/sharedbackgroundvisibility(_:).md)
  Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.
- [func visibilityPriority(ToolbarItemVisibilityPriority) -> some ToolbarContent](toolbarcontent/visibilitypriority(_:).md)
  Defines the visibility priority for a toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarcontent/hidden(_:))*