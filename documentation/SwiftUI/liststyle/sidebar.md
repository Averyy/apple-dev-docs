# sidebar

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The list style that describes the behavior and appearance of a sidebar list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var sidebar: SidebarListStyle { get }
```

Available when `Self` is `SidebarListStyle`.

#### Discussion

On macOS and iOS, the sidebar list style displays disclosure indicators in the section headers that allow the user to collapse and expand sections.

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
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of a list with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle](./inset%28alternatesrowbackgrounds%29.md)
  The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/liststyle/sidebar)*