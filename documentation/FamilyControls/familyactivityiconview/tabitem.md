# tabItem(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the tab bar item associated with this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func tabItem<V>(@ViewBuilder _ label: () -> V) -> some View where V : View
```

#### Discussion

Use `tabItem(_:)` to configure a view as a tab bar item in a `TabView`. The example below adds two views as tabs in a `TabView`:

```swift
struct View1: View {
    var body: some View {
        Text("View 1")
    }
}

struct View2: View {
    var body: some View {
        Text("View 2")
    }
}

struct TabItem: View {
    var body: some View {
        TabView {
            View1()
                .tabItem {
                    Label("Menu", systemImage: "list.dash")
                }

            View2()
                .tabItem {
                    Label("Order", systemImage: "square.and.pencil")
                }
        }
    }
}
```

## Parameters

- `label`: The tab bar item to associate with this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/tabitem(_:))*