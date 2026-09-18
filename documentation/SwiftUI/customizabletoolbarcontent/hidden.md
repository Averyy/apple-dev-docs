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
func hidden(_ hidden: Bool = true) -> some CustomizableToolbarContent
```

#### Discussion

Use this modifier to conditionally display a toolbar item in the toolbar. On macOS, hidden items will be displayed during user customization.

The following example hides a downloads button when there are no downloads, but it is displayed during customization.

```swift
struct ContentView {
    @State private var showDownloads = false

    var body: some View {
        BrowserView()
            .toolbar(id: "browserToolbar") {
                ToolbarItem(id: "downloads") {
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

- [func sharedBackgroundVisibility(Visibility) -> some CustomizableToolbarContent](customizabletoolbarcontent/sharedbackgroundvisibility(_:).md)
  Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.
- [func visibilityPriority(ToolbarItemVisibilityPriority) -> some CustomizableToolbarContent](customizabletoolbarcontent/visibilitypriority(_:).md)
  Defines the visibility priority for a toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/hidden(_:))*