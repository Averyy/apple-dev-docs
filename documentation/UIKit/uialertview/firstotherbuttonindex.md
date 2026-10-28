# firstOtherButtonIndex

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The index of the first other button.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
var firstOtherButtonIndex: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger firstOtherButtonIndex;
```

## Discussion

The button indices start at `0`. If `-1`, then the index is not set. This property is ignored if there are no other buttons. The default value is `-1`.

## See Also

### Configuring buttons
- [func addButton(withTitle: String?) -> Int](./addbutton%28withtitle%29.md)
  Adds a button to the receiver with the given title.
- [var numberOfButtons: Int](./numberofbuttons.md)
  The number of buttons on the alert view.
- [func buttonTitle(at: Int) -> String?](./buttontitle%28at%29.md)
  Returns the title of the button at the given index.
- [func textField(at: Int) -> UITextField?](./textfield%28at%29.md)
  Returns the text field at the given index
- [var cancelButtonIndex: Int](./cancelbuttonindex.md)
  The index number of the cancel button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/firstotherbuttonindex)*