# bordered(alternatesRowBackgrounds:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

The list style that describes the behavior and appearance of a list with standard border.

**Availability**:
- macOS 12.0+ - Deprecated in 27.2

> **Deprecated**: Use the [`bordered`](./bordered.md) style and add the [`alternatingRowBackgrounds(_:)`](../view/alternatingrowbackgrounds%28_%29.md) view modifier instead.

## Declaration

```swift
@export(implementation)
static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle
```

Available when `Self` is `BorderedListStyle`.

#### Discussion

Bordered lists are expected to be inset from their outer containers, but do not have inset style rows or selection.

## Parameters

- `alternatesRowBackgrounds`: Whether the rows should alternate their backgrounds to help visually distinguish them from each other.

## See Also

### Getting built-in list styles
- [static var automatic: DefaultListStyle](./automatic.md)
  The list style that describes a platform’s default behavior and appearance for a list.
- [static var bordered: BorderedListStyle](./bordered.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static var carousel: CarouselListStyle](./carousel.md)
  The carousel list style.
- [static var elliptical: EllipticalListStyle](./elliptical.md)
  The list style that describes the behavior and appearance of an elliptical list.
- [static var grouped: GroupedListStyle](./grouped.md)
  The list style that describes the behavior and appearance of a grouped list.
- [static var inset: InsetListStyle](./inset.md)
  The list style that describes the behavior and appearance of an inset list.
- [static var insetGrouped: InsetGroupedListStyle](./insetgrouped.md)
  The list style that describes the behavior and appearance of an inset grouped list.
- [static var plain: PlainListStyle](./plain.md)
  The list style that describes the behavior and appearance of a plain list.
- [static var sidebar: SidebarListStyle](./sidebar.md)
  The list style that describes the behavior and appearance of a sidebar list.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](./inset%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/bordered(alternatesrowbackgrounds:))*