# sceneBridgingOptions

**Framework**: SwiftUI  
**Kind**: property

The options for which aspects of the window will be managed by this hosting view.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency var sceneBridgingOptions: NSHostingSceneBridgingOptions { get set }
```

#### Discussion

`NSHostingView` will populate certain aspects of its associated window, depending on which options are specified.

For example, a hosting view can manage its window’s toolbar by including the `.toolbars` option:

```swift
struct RootView: View {
    var body: some View {
        ContentView()
            .toolbar {
                MyToolbarContent()
            }
    }
}

let view = NSHostingView(rootView: RootView())
view.sceneBridgingOptions = [.toolbars]
```

When this hosting view is set as the `contentView` for a window, the default value for this property will be `.all`, which includes the options for `.toolbars` and `.title`. Otherwise, the default value is `[]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview/scenebridgingoptions)*