# UIKeyboardCenterEndUserInfoKey

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A user info key to retrieve the center point of the keyboard after its animation completes.

**Availability**:
- iOS 2.0+ - Deprecated in 3.2
- iPadOS 2.0+ - Deprecated in 3.2
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`keyboardFrameEndUserInfoKey`](./uiresponder/keyboardframeenduserinfokey.md) instead.

## Declaration

```c
extern NSString * const UIKeyboardCenterEndUserInfoKey;
```

#### Discussion

The value retrieved with this key is an [`NSValue`](../Foundation/nsvalue.md) object containing a [`CGPoint`](../CoreFoundation/cgpoint.md) indicating the keyboard’s center point, in the window’s coordinate space, after its animation ends. These coordinates take into account any rotation factors applied to the window’s contents as a result of interface orientation changes. Thus, the center point of the keyboard is different in portrait versus landscape orientations.

## See Also

### Deprecated
- [UIKeyboardCenterBeginUserInfoKey](./uikeyboardcenterbeginuserinfokey.md)
  A user info key to retrieve the center point of the keyboard before its animation begins.
- [UIKeyboardBoundsUserInfoKey](./uikeyboardboundsuserinfokey.md)
  A user info key to retrieve the bounds of the keyboard.
- [convenience init()](./uiwindow/init%28%29.md)
- [init(frame: CGRect)](./uiwindow/init%28frame%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardcenterenduserinfokey)*