# elliptical

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The list style that describes the behavior and appearance of an elliptical list.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@export(implementation)
static var elliptical: EllipticalListStyle { get }
```

Available when `Self` is `EllipticalListStyle`.

#### Discussion

On watchOS, the elliptical list style uses a transform for items rolling off the top or bottom of the list, as if on a rounded surface that faces the user.

Apple Watch Series 3 does not support this style and will instead fall back to using the [`plain`](./plain.md) style.

## See Also

### Getting built-in list styles
- [static var automatic: DefaultListStyle](./automatic.md)
  The list style that describes a platform’s default behavior and appearance for a list.
- [static var bordered: BorderedListStyle](./bordered.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static var carousel: CarouselListStyle](./carousel.md)
  The carousel list style.
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
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](./inset%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/elliptical)*