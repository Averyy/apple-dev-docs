# principal

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A placement for the principal item section.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let principal: ToolbarItemPlacement
```

#### Discussion

Principal actions are key units of functionality that receive prominent placement. For example, the location field for a web browser is a principal item.

In macOS and in Mac Catalyst apps, the system places the principal item in the center of the toolbar.

In iOS, iPadOS, and tvOS, the system places the principal item in the center of the navigation bar. This item takes precedent over a title specified through [`navigationTitle(_:)`](../view/navigationtitle%28_%29.md).

## See Also

### Getting semantic placement
- [static let automatic: ToolbarItemPlacement](./automatic.md)
  A placement the system positions automatically.
- [static let status: ToolbarItemPlacement](./status.md)
  A placement for items that represents a change in status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/principal)*