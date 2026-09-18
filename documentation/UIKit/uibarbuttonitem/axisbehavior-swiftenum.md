# UIBarButtonItem.AxisBehavior

**Framework**: UIKit  
**Kind**: enum

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
enum AxisBehavior
```

## Topics

### Choosing an orientation behavior
- [UIBarButtonItem.AxisBehavior.automatic](uibarbuttonitem/axisbehavior-swift.enum/automatic.md)
  The automatic behavior. The system infers the supported axes based on the contents of the item.
- [UIBarButtonItem.AxisBehavior.horizontalOnly](uibarbuttonitem/axisbehavior-swift.enum/horizontalonly.md)
  The item only supports horizontal bars. If an item only supports horizontal bars and no horizontal bars are present, the item is not shown.
- [UIBarButtonItem.AxisBehavior.verticalPreferred](uibarbuttonitem/axisbehavior-swift.enum/verticalpreferred.md)
  The item supports both horizontal and vertical bars, and prefers a vertical placement when both horizontal and vertical bars are present
### Initializers
- [init?(rawValue: Int)](uibarbuttonitem/axisbehavior-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var hidesSharedBackground: Bool](uibarbuttonitem/hidessharedbackground.md)
  A boolean value indicating whether the background this item may share with other items in the bar should be hidden.
- [var sharesBackground: Bool](uibarbuttonitem/sharesbackground.md)
  A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.
- [var axisBehavior: UIBarButtonItem.AxisBehavior](uibarbuttonitem/axisbehavior-swift.property.md)
  The bar axis behavior of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/axisbehavior-swift.enum)*