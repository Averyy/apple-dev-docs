# ListStyle

**Framework**: SwiftUI  
**Kind**: protocol

A protocol that describes the behavior and appearance of a list.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol ListStyle
```

## Topics

### Getting built-in list styles
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
### Deprecated styles
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle](liststyle/bordered(alternatesrowbackgrounds:).md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](liststyle/inset(alternatesrowbackgrounds:).md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.
### Supporting types
- [struct DefaultListStyle](defaultliststyle.md)
  The list style that describes a platform’s default behavior and appearance for a list.
- [struct BorderedListStyle](borderedliststyle.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [struct CarouselListStyle](carouselliststyle.md)
  The carousel list style.
- [struct EllipticalListStyle](ellipticalliststyle.md)
  The list style that describes the behavior and appearance of an elliptical list.
- [struct GroupedListStyle](groupedliststyle.md)
  The list style that describes the behavior and appearance of a grouped list.
- [struct InsetListStyle](insetliststyle.md)
  The list style that describes the behavior and appearance of an inset list.
- [struct InsetGroupedListStyle](insetgroupedliststyle.md)
  The list style that describes the behavior and appearance of an inset grouped list.
- [struct PlainListStyle](plainliststyle.md)
  The list style that describes the behavior and appearance of a plain list.
- [struct SidebarListStyle](sidebarliststyle.md)
  The list style that describes the behavior and appearance of a sidebar list.

## Relationships

### Conforming Types
- [BorderedListStyle](borderedliststyle.md)
- [CarouselListStyle](carouselliststyle.md)
- [DefaultListStyle](defaultliststyle.md)
- [EllipticalListStyle](ellipticalliststyle.md)
- [GroupedListStyle](groupedliststyle.md)
- [InsetGroupedListStyle](insetgroupedliststyle.md)
- [InsetListStyle](insetliststyle.md)
- [PlainListStyle](plainliststyle.md)
- [SidebarListStyle](sidebarliststyle.md)

## See Also

- [func listStyle<S>(S) -> some View](view/liststyle(_:).md)
  Sets the style for lists within this view.
- [func tableStyle<S>(S) -> some View](view/tablestyle(_:).md)
  Sets the style for tables within this view.
- [protocol TableStyle](tablestyle.md)
  A type that applies a custom appearance to all tables within a view.
- [struct TableStyleConfiguration](tablestyleconfiguration.md)
  The properties of a table.
- [func disclosureGroupStyle<S>(S) -> some View](view/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [protocol DisclosureGroupStyle](disclosuregroupstyle.md)
  A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle)*