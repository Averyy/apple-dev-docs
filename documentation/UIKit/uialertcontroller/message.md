# message

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Descriptive text that provides more details about the reason for the alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var message: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * message;
```

#### Discussion

The message string is displayed below the title string and is less prominent. Use this string to provide additional context about the reason for the alert or about the actions that the user might take.

## See Also

### Configuring the alert
- [var title: String?](./title.md)
  The title of the alert.
- [var preferredStyle: UIAlertController.Style](./preferredstyle.md)
  The style of the alert controller.
- [UIAlertController.Style](./style.md)
  Constants indicating the type of alert to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/message)*