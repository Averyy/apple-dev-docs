# topBarLeading

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A placement for items in the leading edge of the top bar.

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
static var topBarLeading: ToolbarItemPlacement { get }
```

## Discussion

On watchOS, iOS, and tvOS, the top bar is the navigation bar.

## See Also

### Getting explicit placement
- [static var topBarTrailing: ToolbarItemPlacement](./topbartrailing.md)
  A placement for items in the trailing edge of the top bar.
- [static let topBarPinnedTrailing: ToolbarItemPlacement](./topbarpinnedtrailing.md)
  A placement that pins the item to the trailing edge of the toolbar.
- [static let bottomBar: ToolbarItemPlacement](./bottombar.md)
  A placement for items in the bottom toolbar.
- [static let bottomOrnament: ToolbarItemPlacement](./bottomornament.md)
  A placement for items in an ornament under the window.
- [static let keyboard: ToolbarItemPlacement](./keyboard.md)
  A placement for items in the keyboard section.
- [static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement](./accessorybar%28id%29.md)
  Creates a unique accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarleading)*