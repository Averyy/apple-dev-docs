# addButton(withTitle:)

**Framework**: UIKit  
**Kind**: method

Adds a button to the receiver with the given title.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func addButton(withTitle title: String?) -> Int
```

#### Return Value

The index of the new button. Button indices start at `0` and increase in the order they are added.

#### Discussion

Adding too many buttons can cause the alert view to scroll. For guidelines on the best ways to use an alert in an app, see [`Temporary Views`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/MobileHIG/Alerts.html#//apple_ref/doc/uid/TP40006556-CH14).

## Parameters

- `title`: The title of the new button.

## See Also

- [var message: String?](uialertview/message.md)
  Descriptive text that provides more details than the title.
- [var numberOfButtons: Int](uialertview/numberofbuttons.md)
  The number of buttons on the alert view.
- [func buttonTitle(at: Int) -> String?](uialertview/buttontitle(at:).md)
  Returns the title of the button at the given index.
- [func textField(at: Int) -> UITextField?](uialertview/textfield(at:).md)
  Returns the text field at the given index
- [var cancelButtonIndex: Int](uialertview/cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](uialertview/firstotherbuttonindex.md)
  The index of the first other button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/addbutton(withtitle:))*