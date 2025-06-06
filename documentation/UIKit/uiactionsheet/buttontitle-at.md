# buttonTitle(at:)

**Framework**: UIKit  
**Kind**: method

Returns the title of the button at the specified index.

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

- [func show(in: UIView)](uiactionsheet/show(in:).md)
  Displays an action sheet that originates from the specified view.
- [func addButton(withTitle: String?) -> Int](uiactionsheet/addbutton(withtitle:).md)
  Adds a custom button to the action sheet.
- [var numberOfButtons: Int](uiactionsheet/numberofbuttons.md)
  The number of buttons on the action sheet.
- [var cancelButtonIndex: Int](uiactionsheet/cancelbuttonindex.md)
  The index number of the cancel button.
- [var destructiveButtonIndex: Int](uiactionsheet/destructivebuttonindex.md)
  The index number of the destructive button.
- [var firstOtherButtonIndex: Int](uiactionsheet/firstotherbuttonindex.md)
  The index of the first custom button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/buttontitle(at:))*