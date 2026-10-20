# verticalPage(transitionStyle:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static func verticalPage(transitionStyle: VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle
```

Available when `Self` is `VerticalPageTabViewStyle`.

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
- [static var verticalPage: VerticalPageTabViewStyle](./verticalpage.md)
  A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [static var carousel: CarouselTabViewStyle](./carousel.md)
  A style that implements the carousel interaction and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewstyle/verticalpage(transitionstyle:))*