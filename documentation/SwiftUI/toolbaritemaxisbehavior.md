# ToolbarItemAxisBehavior

**Framework**: SwiftUI  
**Kind**: struct

Describes the bar axis behavior of a toolbar item.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
struct ToolbarItemAxisBehavior
```

#### Overview

Use this with the [`axisBehavior(_:)`](toolbarcontent/axisbehavior(_:).md) modifier to control which bar axes a toolbar item can appear in.

## Topics

### Getting behavior options
- [static let automatic: ToolbarItemAxisBehavior](toolbaritemaxisbehavior/automatic.md)
  The automatic axis behavior.
- [static let horizontalOnly: ToolbarItemAxisBehavior](toolbaritemaxisbehavior/horizontalonly.md)
  The item only supports horizontal bars. If an item only supports horizontal bars and no horizontal bars are present, the item is not shown.
- [static let verticalPreferred: ToolbarItemAxisBehavior](toolbaritemaxisbehavior/verticalpreferred.md)
  The item supports both horizontal and vertical bars, and prefers a vertical placement when both horizontal and vertical bars are present.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func axisBehavior(ToolbarItemAxisBehavior) -> some ToolbarContent](toolbarcontent/axisbehavior(_:).md)
  The bar axis behavior of the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemaxisbehavior)*