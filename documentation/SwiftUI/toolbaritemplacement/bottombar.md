# bottomBar

**Framework**: SwiftUI  
**Kind**: property

Places the item in the bottom toolbar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let bottomBar: ToolbarItemPlacement
```

#### Discussion

On tvOS, this applies only within the sidebar of a [`NavigationSplitView`](navigationsplitview.md).  It has no effect if used elsewhere.

## See Also

- [static var topBarLeading: ToolbarItemPlacement](toolbaritemplacement/topbarleading.md)
  Places the item in the leading edge of the top bar.
- [static var topBarTrailing: ToolbarItemPlacement](toolbaritemplacement/topbartrailing.md)
  Places the item in the trailing edge of the top bar.
- [static let bottomOrnament: ToolbarItemPlacement](toolbaritemplacement/bottomornament.md)
  Places the item in an ornament under the window.
- [static let keyboard: ToolbarItemPlacement](toolbaritemplacement/keyboard.md)
  The item is placed in the keyboard section.
- [static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement](toolbaritemplacement/accessorybar(id:).md)
  Creates a unique accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/bottombar)*