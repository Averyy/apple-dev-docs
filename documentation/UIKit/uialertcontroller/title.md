# title

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The title of the alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * title;
```

#### Discussion

The title string is displayed prominently in the alert or action sheet. You should use this string to get the user’s attention and communicate the reason for displaying the alert.

## See Also

### Configuring the alert
- [var message: String?](./message.md)
  Descriptive text that provides more details about the reason for the alert.
- [var preferredStyle: UIAlertController.Style](./preferredstyle.md)
  The style of the alert controller.
- [UIAlertController.Style](./style.md)
  Constants indicating the type of alert to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/title)*