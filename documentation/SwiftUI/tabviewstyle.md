# TabViewStyle

**Framework**: SwiftUI  
**Kind**: protocol

A specification for the appearance and interaction of a tab view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol TabViewStyle
```

#### Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting built-in tab view styles
- [static var automatic: DefaultTabViewStyle](tabviewstyle/automatic.md)
  The default tab view style.
- [static var sidebarAdaptable: SidebarAdaptableTabViewStyle](tabviewstyle/sidebaradaptable.md)
  A tab bar style that adapts to each platform.
- [static var tabBarOnly: TabBarOnlyTabViewStyle](tabviewstyle/tabbaronly.md)
  A tab view style that displays a tab bar when possible.
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
### Supporting types
- [struct DefaultTabViewStyle](defaulttabviewstyle.md)
  The default tab view style.
- [struct SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md)
  A tab bar style that adapts to each platform.
- [struct TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md)
  A tab view style that displays a tab bar when possible.
- [struct GroupedTabViewStyle](groupedtabviewstyle.md)
  A tab view style that displays a tab bar that groups its tabs together.
- [struct PageTabViewStyle](pagetabviewstyle.md)
  A `TabViewStyle` that displays a paged scrolling `TabView`.
- [struct VerticalPageTabViewStyle](verticalpagetabviewstyle.md)
  A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [struct CarouselTabViewStyle](carouseltabviewstyle.md)
  A style that implements the carousel interaction and appearance.

## Relationships

### Conforming Types
- [CarouselTabViewStyle](carouseltabviewstyle.md)
- [DefaultTabViewStyle](defaulttabviewstyle.md)
- [GroupedTabViewStyle](groupedtabviewstyle.md)
- [PageTabViewStyle](pagetabviewstyle.md)
- [SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md)
- [TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md)
- [VerticalPageTabViewStyle](verticalpagetabviewstyle.md)

## See Also

- [func navigationSplitViewStyle<S>(S) -> some View](view/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [protocol NavigationSplitViewStyle](navigationsplitviewstyle.md)
  A type that specifies the appearance and interaction of navigation split views within a view hierarchy.
- [func tabViewStyle<S>(S) -> some View](view/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewstyle)*