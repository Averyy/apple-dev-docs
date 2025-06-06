# bordered

**Framework**: SwiftUI  
**Kind**: property

The list style that describes the behavior and appearance of a list with standard border.

**Availability**:
- macOS 12.0+

## Declaration

```swift
static var bordered: BorderedListStyle { get }
```

#### Discussion

Bordered lists are expected to be inset from their outer containers, but do not have inset style rows or selection.

To customize whether the rows of the list should alternate their backgrounds, use [`bordered(alternatesRowBackgrounds:)`](liststyle/bordered(alternatesrowbackgrounds:).md).

## See Also

- [static var automatic: DefaultListStyle](liststyle/automatic.md)
  The list style that describes a platform’s default behavior and appearance for a list.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/bordered)*