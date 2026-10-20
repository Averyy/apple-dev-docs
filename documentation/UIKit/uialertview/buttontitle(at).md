# buttonTitle(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the title of the button at the given index.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
func buttonTitle(at buttonIndex: Int) -> String?
```

```objc
- (NSString *) buttonTitleAtIndex:(NSInteger) buttonIndex;
```

#### Return Value

The title of the button specified by index `buttonIndex`.

## Parameters

- `buttonIndex`: The index of the button. The button indices start at `0`.

## See Also

### Configuring buttons
- [func addButton(withTitle: String?) -> Int](./addbutton%28withtitle%29.md)
  Adds a button to the receiver with the given title.
- [var numberOfButtons: Int](./numberofbuttons.md)
  The number of buttons on the alert view.
- [func textField(at: Int) -> UITextField?](./textfield%28at%29.md)
  Returns the text field at the given index
- [var cancelButtonIndex: Int](./cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](./firstotherbuttonindex.md)
  The index of the first other button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/buttontitle(at:))*