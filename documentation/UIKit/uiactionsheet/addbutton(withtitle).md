# addButton(withTitle:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a custom button to the action sheet.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
func addButton(withTitle title: String?) -> Int
```

```objc
- (NSInteger) addButtonWithTitle:(NSString *) title;
```

#### Return Value

The index of the new button. Button indices start at `0` and increase in the order they are added.

## Parameters

- `title`: The title of the new button.

## See Also

### Related Documentation
- [class UIActionSheet](../uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
### Configuring buttons
- [var numberOfButtons: Int](./numberofbuttons.md)
  The number of buttons on the action sheet.
- [func buttonTitle(at: Int) -> String?](./buttontitle%28at%29.md)
  Returns the title of the button at the specified index.
- [var cancelButtonIndex: Int](./cancelbuttonindex.md)
  The index number of the cancel button.
- [var destructiveButtonIndex: Int](./destructivebuttonindex.md)
  The index number of the destructive button.
- [var firstOtherButtonIndex: Int](./firstotherbuttonindex.md)
  The index of the first custom button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/addbutton(withtitle:))*