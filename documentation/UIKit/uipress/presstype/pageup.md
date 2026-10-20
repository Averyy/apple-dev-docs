# UIPress.PressType.pageUp

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A constant that represents the page up button.

**Availability**:
- tvOS 14.3+

## Declaration

```swift
case pageUp
```

```c
UIPressTypePageUp
```

#### Discussion

Add gesture recognizers for [`UIPress.PressType.pageDown`](./pagedown.md) and [`UIPress.PressType.pageUp`](./pageup.md) to navigate content in your app.

In an electronic program guide, select the item above the current one in response to [`UIPress.PressType.upArrow`](./uparrow.md), and display the previous screen of items in response to [`UIPress.PressType.pageUp`](./pageup.md). While your content plays, change the channel when your app receives [`UIPress.PressType.pageUp`](./pageup.md) or [`UIPress.PressType.pageDown`](./pagedown.md).

For more details on browsing multichannel content, see [Providing Channel Navigation](../../../TVServices/providing-channel-navigation.md).

## See Also

### Navigation
- [UIPress.PressType.upArrow](./uparrow.md)
  A constant that represents the up arrow button.
- [UIPress.PressType.downArrow](./downarrow.md)
  A constant that represents the down arrow button.
- [UIPress.PressType.leftArrow](./leftarrow.md)
  A constant that represents the left arrow button.
- [UIPress.PressType.rightArrow](./rightarrow.md)
  A constant that represents the right arrow button.
- [UIPress.PressType.pageDown](./pagedown.md)
  A constant that represents the page down button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/presstype/pageup)*