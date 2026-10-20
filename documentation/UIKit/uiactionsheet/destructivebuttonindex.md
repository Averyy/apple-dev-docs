# destructiveButtonIndex

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The index number of the destructive button.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
var destructiveButtonIndex: Int { get set }
```

```objc
@property (nonatomic) NSInteger destructiveButtonIndex;
```

#### Discussion

Button indices start at `0`. The default value of this property is normally `-1`, which indicates that no destructive button has been set. However, a destructive button may be created and set automatically by the [`init(title:delegate:cancelButtonTitle:destructiveButtonTitle:)`](./init%28title,delegate,cancelbuttontitle,destructivebuttontitle%29.md) method. If you use that method to create a destructive button, you should not change the value of this property.

## See Also

### Configuring buttons
- [func addButton(withTitle: String?) -> Int](./addbutton%28withtitle%29.md)
  Adds a custom button to the action sheet.
- [var numberOfButtons: Int](./numberofbuttons.md)
  The number of buttons on the action sheet.
- [func buttonTitle(at: Int) -> String?](./buttontitle%28at%29.md)
  Returns the title of the button at the specified index.
- [var cancelButtonIndex: Int](./cancelbuttonindex.md)
  The index number of the cancel button.
- [var firstOtherButtonIndex: Int](./firstotherbuttonindex.md)
  The index of the first custom button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/destructivebuttonindex)*