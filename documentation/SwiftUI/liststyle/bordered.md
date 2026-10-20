# bordered

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The list style that describes the behavior and appearance of a list with standard border.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@export(implementation)
static var bordered: BorderedListStyle { get }
```

Available when `Self` is `BorderedListStyle`.

#### Discussion

Bordered lists are expected to be inset from their outer containers, but do not have inset style rows or selection.

To customize whether the rows of the list should alternate their backgrounds, use [`bordered(alternatesRowBackgrounds:)`](./bordered%28alternatesrowbackgrounds%29.md).

## See Also

### Getting built-in list styles
- [static var automatic: DefaultListStyle](./automatic.md)
  The list style that describes a platform’s default behavior and appearance for a list.
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
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](./inset%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/bordered)*