# firstOtherButtonIndex

**Framework**: UIKit  
**Kind**: property

The index of the first custom button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var firstOtherButtonIndex: Int { get }
```

#### Discussion

Button indices start at `0`. The default value of this property is `-1`, which indicates that there are no other custom buttons.

## See Also

- [func addButton(withTitle: String?) -> Int](uiactionsheet/addbutton(withtitle:).md)
  Adds a custom button to the action sheet.
- [var numberOfButtons: Int](uiactionsheet/numberofbuttons.md)
  The number of buttons on the action sheet.
- [func buttonTitle(at: Int) -> String?](uiactionsheet/buttontitle(at:).md)
  Returns the title of the button at the specified index.
- [var cancelButtonIndex: Int](uiactionsheet/cancelbuttonindex.md)
  The index number of the cancel button.
- [var destructiveButtonIndex: Int](uiactionsheet/destructivebuttonindex.md)
  The index number of the destructive button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/firstotherbuttonindex)*