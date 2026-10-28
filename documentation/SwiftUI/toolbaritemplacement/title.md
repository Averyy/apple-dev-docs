# title

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A placement for items in the title area of the navigation bar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@export(implementation)
static var title: ToolbarItemPlacement { get }
```

## Discussion

The view appears when the navigation bar renders its title inline, and takes precedence over the value provided to the [`navigationTitle(_:)`](../view/navigationtitle%28_%29.md) modifier.

```swift
struct ContentView: View {
    var body: some View {
        NavigationStack {
            DetailView()
                .navigationTitle("Title")
                .navigationSubtitle("Subtitle")
                .toolbar {
                    ToolbarItem(placement: .title) {
                        CustomNavigationTitle()
                    }
                }
        }
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/title)*