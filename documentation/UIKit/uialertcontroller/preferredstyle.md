# preferredStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style of the alert controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var preferredStyle: UIAlertController.Style { get }
```

```objc
@property (nonatomic, readonly) UIAlertControllerStyle preferredStyle;
```

#### Discussion

The value of this property is set to the value you specified in the [`init(title:message:preferredStyle:)`](./init%28title,message,preferredstyle%29.md) method. This value determines how the alert is displayed onscreen.

## See Also

### Configuring the alert
- [var title: String?](./title.md)
  The title of the alert.
- [var message: String?](./message.md)
  Descriptive text that provides more details about the reason for the alert.
- [UIAlertController.Style](./style.md)
  Constants indicating the type of alert to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/preferredstyle)*