# topBarTrailing

**Framework**: SwiftUI  
**Kind**: property

A placement for items in the trailing edge of the top bar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@backDeployed(before: iOS 17.0, tvOS 17.0)
static var topBarTrailing: ToolbarItemPlacement { get }
```

#### Discussion

On watchOS, iOS, and tvOS, the top bar is the navigation bar.

## See Also

- [static var topBarLeading: ToolbarItemPlacement](toolbaritemplacement/topbarleading.md)
  A placement for items in the leading edge of the top bar.
- [static let topBarPinnedTrailing: ToolbarItemPlacement](toolbaritemplacement/topbarpinnedtrailing.md)
  A placement that pins the item to the trailing edge of the toolbar.
- [static let bottomBar: ToolbarItemPlacement](toolbaritemplacement/bottombar.md)
  A placement for items in the bottom toolbar.
- [static let bottomOrnament: ToolbarItemPlacement](toolbaritemplacement/bottomornament.md)
  A placement for items in an ornament under the window.
- [static let keyboard: ToolbarItemPlacement](toolbaritemplacement/keyboard.md)
  A placement for items in the keyboard section.
- [static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement](toolbaritemplacement/accessorybar(id:).md)
  Creates a unique accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbartrailing)*