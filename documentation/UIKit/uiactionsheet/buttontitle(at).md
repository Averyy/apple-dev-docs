# buttonTitle(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the title of the button at the specified index.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
func buttonTitle(at buttonIndex: Int) -> String?
```

```objc
- (NSString *) buttonTitleAtIndex:(NSInteger) buttonIndex;
```

#### Return Value

The title of the button specified by index `buttonIndex`.

## Parameters

- `buttonIndex`: The index of the button. The button indices start at `0`.

## See Also

### Related Documentation
- [func show(in: UIView)](./show%28in%29.md)
  Displays an action sheet that originates from the specified view.
### Configuring buttons
- [func addButton(withTitle: String?) -> Int](./addbutton%28withtitle%29.md)
  Adds a custom button to the action sheet.
- [var numberOfButtons: Int](./numberofbuttons.md)
  The number of buttons on the action sheet.
- [var cancelButtonIndex: Int](./cancelbuttonindex.md)
  The index number of the cancel button.
- [var destructiveButtonIndex: Int](./destructivebuttonindex.md)
  The index number of the destructive button.
- [var firstOtherButtonIndex: Int](./firstotherbuttonindex.md)
  The index of the first custom button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/buttontitle(at:))*