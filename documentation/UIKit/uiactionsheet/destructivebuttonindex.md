# destructiveButtonIndex

**Framework**: UIKit  
**Kind**: property

The index number of the destructive button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var destructiveButtonIndex: Int { get set }
```

#### Discussion

Button indices start at `0`. The default value of this property is normally `-1`, which indicates that no destructive button has been set. However, a destructive button may be created and set automatically by the [`init(title:delegate:cancelButtonTitle:destructiveButtonTitle:)`](uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:).md) method. If you use that method to create a destructive button, you should not change the value of this property.

## See Also

- [func addButton(withTitle: String?) -> Int](uiactionsheet/addbutton(withtitle:).md)
  Adds a custom button to the action sheet.
- [var numberOfButtons: Int](uiactionsheet/numberofbuttons.md)
  The number of buttons on the action sheet.
- [func buttonTitle(at: Int) -> String?](uiactionsheet/buttontitle(at:).md)
  Returns the title of the button at the specified index.
- [var cancelButtonIndex: Int](uiactionsheet/cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](uiactionsheet/firstotherbuttonindex.md)
  The index of the first custom button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/destructivebuttonindex)*