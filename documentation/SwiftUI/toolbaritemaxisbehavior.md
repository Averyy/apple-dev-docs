# ToolbarItemAxisBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Describes the bar axis behavior of a toolbar item.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
struct ToolbarItemAxisBehavior
```

## Overview

Use this with the [`axisBehavior(_:)`](./toolbarcontent/axisbehavior%28_%29.md) modifier to control which bar axes a toolbar item can appear in.

## Topics

### Getting behavior options
- [static let automatic: ToolbarItemAxisBehavior](./toolbaritemaxisbehavior/automatic.md)
  The automatic axis behavior.
- [static let horizontalOnly: ToolbarItemAxisBehavior](./toolbaritemaxisbehavior/horizontalonly.md)
  The item only supports horizontal bars. If an item only supports horizontal bars and no horizontal bars are present, the item is not shown.
- [static let verticalPreferred: ToolbarItemAxisBehavior](./toolbaritemaxisbehavior/verticalpreferred.md)
  The item supports both horizontal and vertical bars, and prefers a vertical placement when both horizontal and vertical bars are present.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Customizing behaviors
- [func axisBehavior(ToolbarItemAxisBehavior) -> some ToolbarContent](./toolbarcontent/axisbehavior%28_%29.md)
  The bar axis behavior of the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemaxisbehavior)*