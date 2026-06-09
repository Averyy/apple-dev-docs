# colorSpaceDidChangeNotification

**Framework**: AppKit  
**Kind**: property

Posted when the color space of the screen has changed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class let colorSpaceDidChangeNotification: NSNotification.Name
```

#### Discussion

The notification object is the [`NSScreen`](nsscreen.md) object whose [`colorSpace`](nsscreen/colorspace.md) has changed.. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [`NSScreen.ColorSpaceDidChangeMessage`](nsscreen/colorspacedidchangemessage.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/colorspacedidchangenotification)*