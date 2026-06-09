# topBarPinnedTrailing

**Framework**: SwiftUI  
**Kind**: property

A placement that pins the item to the trailing edge of the toolbar.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let topBarPinnedTrailing: ToolbarItemPlacement
```

#### Discussion

Pinned items only move to the overflow menu when search is active and there isn’t enough room.

On iOS and visionOS, the top bar is the navigation bar.

## See Also

- [static var topBarLeading: ToolbarItemPlacement](toolbaritemplacement/topbarleading.md)
  A placement for items in the leading edge of the top bar.
- [static var topBarTrailing: ToolbarItemPlacement](toolbaritemplacement/topbartrailing.md)
  A placement for items in the trailing edge of the top bar.
- [static let bottomBar: ToolbarItemPlacement](toolbaritemplacement/bottombar.md)
  A placement for items in the bottom toolbar.
- [static let bottomOrnament: ToolbarItemPlacement](toolbaritemplacement/bottomornament.md)
  A placement for items in an ornament under the window.
- [static let keyboard: ToolbarItemPlacement](toolbaritemplacement/keyboard.md)
  A placement for items in the keyboard section.
- [static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement](toolbaritemplacement/accessorybar(id:).md)
  Creates a unique accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarpinnedtrailing)*