# addButton(withTitle:)

**Framework**: UIKit  
**Kind**: method

Adds a custom button to the action sheet.

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

## Parameters

- `title`: The title of the new button.

## See Also

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [var numberOfButtons: Int](uiactionsheet/numberofbuttons.md)
  The number of buttons on the action sheet.
- [func buttonTitle(at: Int) -> String?](uiactionsheet/buttontitle(at:).md)
  Returns the title of the button at the specified index.
- [var cancelButtonIndex: Int](uiactionsheet/cancelbuttonindex.md)
  The index number of the cancel button.
- [var destructiveButtonIndex: Int](uiactionsheet/destructivebuttonindex.md)
  The index number of the destructive button.
- [var firstOtherButtonIndex: Int](uiactionsheet/firstotherbuttonindex.md)
  The index of the first custom button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/addbutton(withtitle:))*