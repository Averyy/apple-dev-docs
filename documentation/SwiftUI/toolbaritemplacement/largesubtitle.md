# largeSubtitle

**Framework**: SwiftUI  
**Kind**: property

Places the item in the subtitle area of the navigation bar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
static let largeSubtitle: ToolbarItemPlacement
```

#### Discussion

The view will be shown either when the navigation bar renders its title out-of-line, and takes precedence over the value provided to the `View.navigationSubtitle(_:)` modifier.

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            DetailView()
                .navigationTitle("Title")
                .navigationSubtitle("Subtitle")
                .toolbar {
                    ToolbarItem(placement: .largeSubtitle) {
                        CustomLargeNavigationSubtitle()
                    }
                }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/largesubtitle)*