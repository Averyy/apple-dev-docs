# TabPlacement

**Framework**: SwiftUI  
**Kind**: struct

A place that a tab can appear.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct TabPlacement
```

#### Overview

Not all `TabView` styles support all placements.

## Topics

### Type Properties
- [static let automatic: TabPlacement](tabplacement/automatic.md)
  The default tab location.
- [static let pinned: TabPlacement](tabplacement/pinned.md)
  The pinned tab placement location.
- [static let sidebarOnly: TabPlacement](tabplacement/sidebaronly.md)
  The sidebar tab placement location.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func sectionActions<Content>(content: () -> Content) -> some View](view/sectionactions(content:).md)
  Adds custom actions to a section.
- [struct TabContentBuilder](tabcontentbuilder.md)
  A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [protocol TabContent](tabcontent.md)
  A type that provides content for programmatically selectable tabs in a tab view.
- [struct AnyTabContent](anytabcontent.md)
  Type erased tab content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabplacement)*