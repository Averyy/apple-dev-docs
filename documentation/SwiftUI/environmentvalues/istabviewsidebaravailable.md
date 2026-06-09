# isTabViewSidebarAvailable

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether a tab sidebar is available within the content of a surrounding [`TabView`](tabview.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var isTabViewSidebarAvailable: Bool { get }
```

#### Discussion

This value is only meaningful inside the content views of a [`TabView`](tabview.md) that uses a sidebar-capable style such as [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md). Reading it from a view that is not nested inside a `TabView`’s content — for example, a view above the `TabView` in the hierarchy — returns `false`.

```swift
struct ContentView: View {
    var body: some View {
        TabView {
            Tab("Home", systemImage: "house") {
                HomeTab()
            }
        }
        .tabViewStyle(.sidebarAdaptable)
    }
}

struct HomeTab: View {
    @Environment(\.isTabViewSidebarAvailable)
    private var isTabViewSidebarAvailable

    var body: some View {
        if isTabViewSidebarAvailable {
            // Sidebar is (or can become) visible — adjust UI.
        } else {
            // No sidebar in this context.
        }
    }
}
```

Use this value to gate behaviors or UI that depend on the sidebar’s availability, rather than inspecting size classes directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/istabviewsidebaravailable)*