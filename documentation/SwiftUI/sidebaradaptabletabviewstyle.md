# SidebarAdaptableTabViewStyle

**Framework**: SwiftUI  
**Kind**: struct

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
struct SidebarAdaptableTabViewStyle
```

#### Overview

Tab views using the sidebar adaptable style have an appearance that varies depending on the platform:

- iPadOS displays a top tab bar that can adapt into a sidebar.
- iOS displays a bottom tab bar.
- macOS and tvOS always show a sidebar.
- visionOS shows an ornament and also shows a sidebar for secondary tabs within a [`TabSection`](tabsection.md).

Use [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [`tabViewStyle(_:)`](view/tabviewstyle(_:).md) modifier.

## Topics

### Initializers
- [init()](sidebaradaptabletabviewstyle/init.md)

## Relationships

### Conforms To
- [TabViewStyle](tabviewstyle.md)

## See Also

- [struct DefaultTabViewStyle](defaulttabviewstyle.md)
  The default tab view style.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sidebaradaptabletabviewstyle)*