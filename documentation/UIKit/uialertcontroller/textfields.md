# textFields

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The array of text fields displayed by the alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var textFields: [UITextField]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<UITextField *> * textFields;
```

## Discussion

Use this property to access the text fields displayed by the alert. The text fields are in the order in which you added them to the alert controller. This order also corresponds to the order in which they are displayed in the alert.

## See Also

### Configuring text fields
- [func addTextField(configurationHandler: ((UITextField) -> Void)?)](./addtextfield%28configurationhandler%29.md)
  Adds a text field to an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/textfields)*