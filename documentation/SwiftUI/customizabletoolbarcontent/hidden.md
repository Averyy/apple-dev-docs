# hidden(_:)

**Framework**: SwiftUI  
**Kind**: method

Hides a toolbar item within its toolbar.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func hidden(_ hidden: Bool = true) -> some CustomizableToolbarContent
```

#### Discussion

Use this modifier to conditionally display a toolbar item in its toolbar. On macOS and iOS, hidden items will be displayed during user customization.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent/hidden(_:))*