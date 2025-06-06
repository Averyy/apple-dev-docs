# VerticalPageTabViewStyle

**Framework**: SwiftUI  
**Kind**: struct

A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
struct VerticalPageTabViewStyle
```

#### Overview

Use [`verticalPage`](tabviewstyle/verticalpage.md) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [`tabViewStyle(_:)`](view/tabviewstyle(_:).md) modifier.

## Topics

### Creating the tab view style
- [init()](verticalpagetabviewstyle/init.md)
- [init(transitionStyle: VerticalPageTabViewStyle.TransitionStyle)](verticalpagetabviewstyle/init(transitionstyle:).md)
  Creates a new `VerticalPageTabViewStyle` with a transition style.
- [VerticalPageTabViewStyle.TransitionStyle](verticalpagetabviewstyle/transitionstyle.md)
  A transition style used between tabs.

## Relationships

### Conforms To
- [TabViewStyle](tabviewstyle.md)

## See Also

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
- [struct CarouselTabViewStyle](carouseltabviewstyle.md)
  A style that implements the carousel interaction and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/verticalpagetabviewstyle)*