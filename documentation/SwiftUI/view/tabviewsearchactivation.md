# tabViewSearchActivation(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the activation and deactivation behavior of search in the search tab.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
nonisolated
func tabViewSearchActivation(_ activation: TabSearchActivation) -> some View
```

#### Discussion

Use this modifier on a [`TabView`](tabview.md) to change how search activation is handled. The exact activation behavior is determined by the [`TabSearchActivation`](tabsearchactivation.md) you pass to this modifier:

```swift
struct TabExampleView: View {
    @State private var text: String = ""

    var body: some View {
        TabView {
            Tab("Books", systemImage: "book") {
                BooksTab()
            }
            Tab(role: .search) {
                NavigationStack {
                    SearchContent()
                }
            }
        }
        .searchable(text: $text)
        .tabViewSearchActivation(.searchTabSelection)
    }
}
```

By default, search is only activated and deactivated by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabviewsearchactivation(_:))*