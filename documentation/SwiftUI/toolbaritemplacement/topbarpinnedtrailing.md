# topBarPinnedTrailing

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A placement that pins the item to the trailing edge of the toolbar.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
static let topBarPinnedTrailing: ToolbarItemPlacement
```

## Discussion

Pinned items only move to the overflow menu when search is active and there isn’t enough room.

On iOS and visionOS, the top bar is the navigation bar.

## See Also

### Getting explicit placement
- [static var topBarLeading: ToolbarItemPlacement](./topbarleading.md)
  A placement for items in the leading edge of the top bar.
- [static var topBarTrailing: ToolbarItemPlacement](./topbartrailing.md)
  A placement for items in the trailing edge of the top bar.
- [static let bottomBar: ToolbarItemPlacement](./bottombar.md)
  A placement for items in the bottom toolbar.
- [static let bottomOrnament: ToolbarItemPlacement](./bottomornament.md)
  A placement for items in an ornament under the window.
- [static let keyboard: ToolbarItemPlacement](./keyboard.md)
  A placement for items in the keyboard section.
- [static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement](./accessorybar%28id%29.md)
  Creates a unique accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarpinnedtrailing)*