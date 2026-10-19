# bordered(alternatesRowBackgrounds:)

**Framework**: SwiftUI  
**Kind**: method

The list style that describes the behavior and appearance of a list with standard border.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@export(implementation)
static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle
```

#### Discussion

Bordered lists are expected to be inset from their outer containers, but do not have inset style rows or selection.

## Parameters

- `alternatesRowBackgrounds`: Whether the rows should alternate their backgrounds to help visually distinguish them from each other.

## See Also

- [static var automatic: DefaultListStyle](liststyle/automatic.md)
  The list style that describes a platform’s default behavior and appearance for a list.
- [static var bordered: BorderedListStyle](liststyle/bordered.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static var carousel: CarouselListStyle](liststyle/carousel.md)
  The carousel list style.
- [static var elliptical: EllipticalListStyle](liststyle/elliptical.md)
  The list style that describes the behavior and appearance of an elliptical list.
- [static var grouped: GroupedListStyle](liststyle/grouped.md)
  The list style that describes the behavior and appearance of a grouped list.
- [static var inset: InsetListStyle](liststyle/inset.md)
  The list style that describes the behavior and appearance of an inset list.
- [static var insetGrouped: InsetGroupedListStyle](liststyle/insetgrouped.md)
  The list style that describes the behavior and appearance of an inset grouped list.
- [static var plain: PlainListStyle](liststyle/plain.md)
  The list style that describes the behavior and appearance of a plain list.
- [static var sidebar: SidebarListStyle](liststyle/sidebar.md)
  The list style that describes the behavior and appearance of a sidebar list.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](liststyle/inset(alternatesrowbackgrounds:).md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/bordered(alternatesrowbackgrounds:))*