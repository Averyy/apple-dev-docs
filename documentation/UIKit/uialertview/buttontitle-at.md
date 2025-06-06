# buttonTitle(at:)

**Framework**: UIKit  
**Kind**: method

Returns the title of the button at the given index.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func buttonTitle(at buttonIndex: Int) -> String?
```

#### Return Value

The title of the button specified by index `buttonIndex`.

## Parameters

- `buttonIndex`: The index of the button. The button indices start at  .

## See Also

- [func addButton(withTitle: String?) -> Int](uialertview/addbutton(withtitle:).md)
  Adds a button to the receiver with the given title.
- [var numberOfButtons: Int](uialertview/numberofbuttons.md)
  The number of buttons on the alert view.
- [func textField(at: Int) -> UITextField?](uialertview/textfield(at:).md)
  Returns the text field at the given index
- [var cancelButtonIndex: Int](uialertview/cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](uialertview/firstotherbuttonindex.md)
  The index of the first other button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/buttontitle(at:))*