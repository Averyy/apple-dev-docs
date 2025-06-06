# cancelButtonIndex

**Framework**: UIKit  
**Kind**: property

The index number of the cancel button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var cancelButtonIndex: Int { get set }
```

#### Discussion

The button indices start at `0`. If `-1`, then the index is not set.

## See Also

- [func addButton(withTitle: String?) -> Int](uialertview/addbutton(withtitle:).md)
  Adds a button to the receiver with the given title.
- [var numberOfButtons: Int](uialertview/numberofbuttons.md)
  The number of buttons on the alert view.
- [func buttonTitle(at: Int) -> String?](uialertview/buttontitle(at:).md)
  Returns the title of the button at the given index.
- [func textField(at: Int) -> UITextField?](uialertview/textfield(at:).md)
  Returns the text field at the given index
- [var firstOtherButtonIndex: Int](uialertview/firstotherbuttonindex.md)
  The index of the first other button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertview/cancelbuttonindex)*