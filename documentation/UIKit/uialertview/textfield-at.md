# textField(at:)

**Framework**: UIKit  
**Kind**: method

Returns the text field at the given index

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func textField(at textFieldIndex: Int) -> UITextField?
```

#### Return Value

The text field specified by index `textFieldIndex`.

#### Discussion

The number of text fields present in an alert is dependent on the style of the alert.

| Alert Style | Text Fields |
| --- | --- |
| [`UIAlertViewStyle.default`](uialertviewstyle/default.md) | No user-editable text fields. |
| [`UIAlertViewStyle.secureTextInput`](uialertviewstyle/securetextinput.md) | A single text field at index `0`. |
| [`UIAlertViewStyle.plainTextInput`](uialertviewstyle/plaintextinput.md) | A single text field at index `0`. |
| [`UIAlertViewStyle.loginAndPasswordInput`](uialertviewstyle/loginandpasswordinput.md) | The login field is at index `0`. The password field is at index `1`. |

If your application attempts to retrieve a text field with an index that is out of bounds, the alert raises an [`rangeException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/rangeException).

## Parameters

- `textFieldIndex`: The index of the text field. The text field indices start at  .

## See Also

- [func addButton(withTitle: String?) -> Int](uialertview/addbutton(withtitle:).md)
  Adds a button to the receiver with the given title.
- [var numberOfButtons: Int](uialertview/numberofbuttons.md)
  The number of buttons on the alert view.
- [func buttonTitle(at: Int) -> String?](uialertview/buttontitle(at:).md)
  Returns the title of the button at the given index.
- [var cancelButtonIndex: Int](uialertview/cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](uialertview/firstotherbuttonindex.md)
  The index of the first other button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/textfield(at:))*