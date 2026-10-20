# UIAlertController.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of alert to display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum Style
```

```c
enum UIAlertControllerStyle : NSInteger;
```

## Topics

### Constants
- [UIAlertController.Style.actionSheet](./style/actionsheet.md)
  An action sheet displayed by the view controller that presented it.
- [UIAlertController.Style.alert](./style/alert.md)
  An alert displayed modally for the app.
### Initializers
- [init?(rawValue: Int)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the alert
- [var title: String?](./title.md)
  The title of the alert.
- [var message: String?](./message.md)
  Descriptive text that provides more details about the reason for the alert.
- [var preferredStyle: UIAlertController.Style](./preferredstyle.md)
  The style of the alert controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/style)*