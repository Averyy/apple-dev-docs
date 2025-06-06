# tabItem(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the tab bar item associated with this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func tabItem<V>(@ViewBuilder _ label: () -> V) -> some View where V : View
```

#### Discussion

Use `tabItem(_:)` to configure a view as a tab bar item in a [`TabView`](tabview.md). The example below adds two views as tabs in a [`TabView`](tabview.md):

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

![A screenshot of a two views configured as tab items in a tab](https://docs-assets.developer.apple.com/published/31a47e769ee8bf9c15e5ac357c73020e/SwiftUI-View-tabItem%402x.png)

## Parameters

- `label`: The tab bar item to associate with this view.

## See Also

- [struct NavigationView](navigationview.md)
  A view for presenting a stack of views that represents a visible path in a navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabitem(_:))*