# verticalPage

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var verticalPage: VerticalPageTabViewStyle { get }
```

Available when `Self` is `VerticalPageTabViewStyle`.

#### Discussion

To apply this style to a tab view, or to a view that contains tab views, use the [`tabViewStyle(_:)`](../view/tabviewstyle%28_%29.md) modifier.

## See Also

### Getting built-in tab view styles
- [static var automatic: DefaultTabViewStyle](./automatic.md)
  The default tab view style.
- [static var sidebarAdaptable: SidebarAdaptableTabViewStyle](./sidebaradaptable.md)
  A tab bar style that adapts to each platform.
- [static var tabBarOnly: TabBarOnlyTabViewStyle](./tabbaronly.md)
  A tab view style that displays a tab bar when possible.
- [static var grouped: GroupedTabViewStyle](./grouped.md)
  A tab view style that displays a tab bar that groups its tabs together.
- [static var page: PageTabViewStyle](./page.md)
  A `TabViewStyle` that displays a paged scrolling `TabView`.
- [static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) -> PageTabViewStyle](./page%28indexdisplaymode%29.md)
  A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [static func verticalPage(transitionStyle: VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle](./verticalpage%28transitionstyle%29.md)
  A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [static var carousel: CarouselTabViewStyle](./carousel.md)
  A style that implements the carousel interaction and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewstyle/verticalpage)*