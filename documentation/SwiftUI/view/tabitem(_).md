# tabItem(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the tab bar item associated with this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use `Tab(title:image:value:content:)` and related initializers instead

## Declaration

```swift
nonisolated
func tabItem<V>(@ContentBuilder _ label: () -> V) -> some View where V : View
```

#### Discussion

Use `tabItem(_:)` to configure a view as a tab bar item in a [`TabView`](../tabview.md). The example below adds two views as tabs in a [`TabView`](../tabview.md):

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

![A screenshot of a two views configured as tab items in a tab](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-tabItem@2x.png)

## Parameters

- `label`: The tab bar item to associate with this view.

## See Also

### Presenting views in tabs
- [Enhancing your app’s content with tab navigation](../enhancing-your-app-content-with-tab-navigation.md)
  Keep your app content front and center while providing quick access to navigation using the tab bar.
- [struct TabView](../tabview.md)
  A view that switches between multiple child views using interactive user interface elements.
- [struct Tab](../tab.md)
  The content for a tab and the tab’s associated tab item in a tab view.
- [struct TabRole](../tabrole.md)
  A value that defines the purpose of the tab.
- [struct TabSection](../tabsection.md)
  A container that you can use to add hierarchy within a tab view.
- [func tabViewStyle<S>(S) -> some View](./tabviewstyle%28_%29.md)
  Sets the style for the tab view within the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabitem(_:))*