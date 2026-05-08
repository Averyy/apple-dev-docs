# elliptical

**Framework**: SwiftUI  
**Kind**: property

The list style that describes the behavior and appearance of an elliptical list.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
static var elliptical: EllipticalListStyle { get }
```

#### Discussion

On watchOS, the elliptical list style uses a transform for items rolling off the top or bottom of the list, as if on a rounded surface that faces the user.

Apple Watch Series 3 does not support this style and will instead fall back to using the [`plain`](liststyle/plain.md) style.

## See Also

- [static var automatic: DefaultListStyle](liststyle/automatic.md)
  The list style that describes a platform’s default behavior and appearance for a list.
- [static var bordered: BorderedListStyle](liststyle/bordered.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static var carousel: CarouselListStyle](liststyle/carousel.md)
  The carousel list style.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/elliptical)*