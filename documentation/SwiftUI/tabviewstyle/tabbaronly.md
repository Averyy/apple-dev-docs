# tabBarOnly

**Framework**: SwiftUI  
**Kind**: property

A tab view style that displays a tab bar when possible.

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
@preconcurrency static var tabBarOnly: TabBarOnlyTabViewStyle { get }
```

#### Discussion

To apply this style to a tab view, or to a view that contains tab views, use the [`tabViewStyle(_:)`](view/tabviewstyle(_:).md) modifier.

## See Also

- [static var automatic: DefaultTabViewStyle](tabviewstyle/automatic.md)
  The default tab view style.
- [static var sidebarAdaptable: SidebarAdaptableTabViewStyle](tabviewstyle/sidebaradaptable.md)
  A tab bar style that adapts to each platform.
- [static var grouped: GroupedTabViewStyle](tabviewstyle/grouped.md)
  A tab view style that displays a tab bar that groups its tabs together.
- [static var page: PageTabViewStyle](tabviewstyle/page.md)
  A `TabViewStyle` that displays a paged scrolling `TabView`.
- [static func page(indexDisplayMode: PageTabViewStyle.IndexDisplayMode) -> PageTabViewStyle](tabviewstyle/page(indexdisplaymode:).md)
  A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [static var verticalPage: VerticalPageTabViewStyle](tabviewstyle/verticalpage.md)
  A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [static func verticalPage(transitionStyle: VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle](tabviewstyle/verticalpage(transitionstyle:).md)
  A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [static var carousel: CarouselTabViewStyle](tabviewstyle/carousel.md)
  A style that implements the carousel interaction and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewstyle/tabbaronly)*