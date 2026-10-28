# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The automatic axis behavior.

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
static let automatic: ToolbarItemAxisBehavior
```

## Discussion

The system infers the supported axes based on the content type of the item. Image items support both axes; text and custom view items support only the horizontal axis.

## See Also

### Getting behavior options
- [static let horizontalOnly: ToolbarItemAxisBehavior](./horizontalonly.md)
  The item only supports horizontal bars. If an item only supports horizontal bars and no horizontal bars are present, the item is not shown.
- [static let verticalPreferred: ToolbarItemAxisBehavior](./verticalpreferred.md)
  The item supports both horizontal and vertical bars, and prefers a vertical placement when both horizontal and vertical bars are present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemaxisbehavior/automatic)*