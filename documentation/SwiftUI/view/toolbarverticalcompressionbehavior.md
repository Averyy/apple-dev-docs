# toolbarVerticalCompressionBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets how bars should compress when different types of toolbars are hosted together and space is constrained.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
func toolbarVerticalCompressionBehavior(_ behavior: ToolbarVerticalCompressionBehavior) -> some View
```

#### Discussion

For example, a productivity-focused app like Files could ensure its toolbar items are preferred over the tab bar:

```swift
struct ContentView: View {
    var body: some View {
        TabView {
            Tab("Recents") {
                NavigationStack {
                    RootView()
                        .toolbar {
                            Button("Up", systemImage: "chevron.up") {
                            }
                            Button("Down", systemImage: "chevron.down") {
                            }
                        }
                        .toolbarVerticalCompressionBehavior(.prefersToolbarItems)
                }
            }
        }
    }
}
```

## See Also

- [func toolbarVerticalBehavior(ToolbarVerticalBehavior) -> some View](view/toolbarverticalbehavior(_:).md)
  Sets the behavior for the vertical bar.
- [struct ToolbarVerticalBehavior](toolbarverticalbehavior.md)
  A behavior that determines whether the vertical bar is used.
- [struct ToolbarVerticalCompressionBehavior](toolbarverticalcompressionbehavior.md)
  A behavior that determines how bars compress when the system places different types of bars together and space is constrained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbarverticalcompressionbehavior(_:))*