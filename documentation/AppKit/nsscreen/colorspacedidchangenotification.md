# colorSpaceDidChangeNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted when the color space of the screen has changed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class let colorSpaceDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const NSScreenColorSpaceDidChangeNotification;
```

## Discussion

The notification object is the [`NSScreen`](../nsscreen.md) object whose [`colorSpace`](./colorspace.md) has changed.. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSScreen.ColorSpaceDidChangeMessage`](./colorspacedidchangemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/colorspacedidchangenotification)*