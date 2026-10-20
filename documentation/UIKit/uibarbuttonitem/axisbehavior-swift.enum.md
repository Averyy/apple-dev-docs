# UIBarButtonItem.AxisBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
enum AxisBehavior
```

```c
enum UIBarButtonItemAxisBehavior : NSInteger;
```

## Topics

### Choosing an orientation behavior
- [UIBarButtonItem.AxisBehavior.automatic](./axisbehavior-swift.enum/automatic.md)
  The automatic behavior. The system infers the supported axes based on the contents of the item.
- [UIBarButtonItem.AxisBehavior.horizontalOnly](./axisbehavior-swift.enum/horizontalonly.md)
  The item only supports horizontal bars. If an item only supports horizontal bars and no horizontal bars are present, the item is not shown.
- [UIBarButtonItem.AxisBehavior.verticalPreferred](./axisbehavior-swift.enum/verticalpreferred.md)
  The item supports both horizontal and vertical bars, and prefers a vertical placement when both horizontal and vertical bars are present
### Initializers
- [init?(rawValue: Int)](./axisbehavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing placement in a toolbar
- [var hidesSharedBackground: Bool](./hidessharedbackground.md)
  A boolean value indicating whether the background this item may share with other items in the bar should be hidden.
- [var sharesBackground: Bool](./sharesbackground.md)
  A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.
- [var axisBehavior: UIBarButtonItem.AxisBehavior](./axisbehavior-swift.property.md)
  The bar axis behavior of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/axisbehavior-swift.enum)*