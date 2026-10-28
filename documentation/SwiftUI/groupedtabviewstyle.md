# GroupedTabViewStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A tab view style that displays a tab bar that groups its tabs together.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
struct GroupedTabViewStyle
```

## Overview

Use [`grouped`](./tabviewstyle/grouped.md) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [`tabViewStyle(_:)`](./view/tabviewstyle%28_%29.md) modifier.

## Topics

### Initializers
- [init()](./groupedtabviewstyle/init%28%29.md)

## Relationships

### Conforms To
- [TabViewStyle](./tabviewstyle.md)

## See Also

### Supporting types
- [struct DefaultTabViewStyle](./defaulttabviewstyle.md)
  The default tab view style.
- [struct SidebarAdaptableTabViewStyle](./sidebaradaptabletabviewstyle.md)
  A tab bar style that adapts to each platform.
- [struct TabBarOnlyTabViewStyle](./tabbaronlytabviewstyle.md)
  A tab view style that displays a tab bar when possible.
- [struct PageTabViewStyle](./pagetabviewstyle.md)
  A `TabViewStyle` that displays a paged scrolling `TabView`.
- [struct VerticalPageTabViewStyle](./verticalpagetabviewstyle.md)
  A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [struct CarouselTabViewStyle](./carouseltabviewstyle.md)
  A style that implements the carousel interaction and appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupedtabviewstyle)*