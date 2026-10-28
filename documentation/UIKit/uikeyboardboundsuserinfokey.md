# UIKeyboardBoundsUserInfoKey

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A user info key to retrieve the bounds of the keyboard.

**Availability**:
- iOS 2.0+ - Deprecated in 3.2
- iPadOS 2.0+ - Deprecated in 3.2
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`keyboardFrameBeginUserInfoKey`](./uiresponder/keyboardframebeginuserinfokey.md) or [`keyboardFrameEndUserInfoKey`](./uiresponder/keyboardframeenduserinfokey.md) instead.

## Declaration

```c
extern NSString * const UIKeyboardBoundsUserInfoKey;
```

## Discussion

The value for this key is an [`NSValue`](../Foundation/nsvalue.md) object containing a [`CGRect`](../CoreFoundation/cgrect.md) that identifies the bounds rectangle of the keyboard in the window coordinate space. This value is sufficient for obtaining the size of the keyboard. If you want to get the origin of the keyboard on the screen (before or after animation), use the values obtained from the user info dictionary through the [`UIKeyboardCenterBeginUserInfoKey`](./uikeyboardcenterbeginuserinfokey.md) or [`UIKeyboardCenterEndUserInfoKey`](./uikeyboardcenterenduserinfokey.md) constants.

## See Also

### Deprecated
- [UIKeyboardCenterBeginUserInfoKey](./uikeyboardcenterbeginuserinfokey.md)
  A user info key to retrieve the center point of the keyboard before its animation begins.
- [UIKeyboardCenterEndUserInfoKey](./uikeyboardcenterenduserinfokey.md)
  A user info key to retrieve the center point of the keyboard after its animation completes.
- [convenience init()](./uiwindow/init%28%29.md)
- [init(frame: CGRect)](./uiwindow/init%28frame%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardboundsuserinfokey)*