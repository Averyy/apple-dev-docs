# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The list style that describes a platform’s default behavior and appearance for a list.

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
@export(implementation)
static var automatic: DefaultListStyle { get }
```

Available when `Self` is `DefaultListStyle`.

## See Also

### Getting built-in list styles
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
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](./inset%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/automatic)*