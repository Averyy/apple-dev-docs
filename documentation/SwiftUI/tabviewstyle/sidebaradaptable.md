# sidebarAdaptable

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A tab bar style that adapts to each platform.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var sidebarAdaptable: SidebarAdaptableTabViewStyle { get }
```

Available when `Self` is `SidebarAdaptableTabViewStyle`.

#### Discussion

Tab views using the sidebar adaptable style have an appearance that varies depending on the platform:

- iPadOS displays a top tab bar that can adapt into a sidebar.
- iOS displays a bottom tab bar.
- macOS and tvOS always show a sidebar.
- visionOS shows an ornament and also shows a sidebar for secondary tabs within a [`TabSection`](../tabsection.md).

To apply this style to a tab view, or to a view that contains tab views, use the [`tabViewStyle(_:)`](../view/tabviewstyle%28_%29.md) modifier.

## See Also

### Getting built-in tab view styles
- [static var automatic: DefaultTabViewStyle](./automatic.md)
  The default tab view style.
- [static var tabBarOnly: TabBarOnlyTabViewStyle](./tabbaronly.md)
  A tab view style that displays a tab bar when possible.
- [static var grouped: GroupedTabViewStyle](./grouped.md)
  A tab view style that displays a tab bar that groups its tabs together.
- [static var page: PageTabViewStyle](./page.md)
  A `TabViewStyle` that displays a paged scrolling `TabView`.
- [static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) -> PageTabViewStyle](./page%28indexdisplaymode%29.md)
  A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [static var verticalPage: VerticalPageTabViewStyle](./verticalpage.md)
  A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [static func verticalPage(transitionStyle: VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle](./verticalpage%28transitionstyle%29.md)
  A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [static var carousel: CarouselTabViewStyle](./carousel.md)
  A style that implements the carousel interaction and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable)*