# addButton(withTitle:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a button to the receiver with the given title.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
func addButton(withTitle title: String?) -> Int
```

```objc
- (NSInteger) addButtonWithTitle:(NSString *) title;
```

#### Return Value

The index of the new button. Button indices start at `0` and increase in the order they are added.

#### Discussion

Adding too many buttons can cause the alert view to scroll. For guidelines on the best ways to use an alert in an app, see [Temporary Views](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/MobileHIG/Alerts.html#//apple_ref/doc/uid/TP40006556-CH14).

## Parameters

- `title`: The title of the new button.

## See Also

### Related Documentation
- [var message: String?](./message.md)
  Descriptive text that provides more details than the title.
### Configuring buttons
- [var numberOfButtons: Int](./numberofbuttons.md)
  The number of buttons on the alert view.
- [func buttonTitle(at: Int) -> String?](./buttontitle%28at%29.md)
  Returns the title of the button at the given index.
- [func textField(at: Int) -> UITextField?](./textfield%28at%29.md)
  Returns the text field at the given index
- [var cancelButtonIndex: Int](./cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](./firstotherbuttonindex.md)
  The index of the first other button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/addbutton(withtitle:))*