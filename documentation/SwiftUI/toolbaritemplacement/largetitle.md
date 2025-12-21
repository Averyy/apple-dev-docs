# largeTitle

**Framework**: SwiftUI  
**Kind**: property

Places the item in the title area of the navigation bar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
static let largeTitle: ToolbarItemPlacement
```

#### Discussion

The view will be shown when the navigation bar renders its title out-of-line, and takes precedence over the value provided to the `View.navigationTitle(_:)` modifier.

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            DetailView()
                .navigationTitle("Title")
                .navigationSubtitle("Subtitle")
                .toolbar {
                    ToolbarItem(placement: .largeTitle) {
                        CustomLargeNavigationTitle()
                    }
                }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/largetitle)*