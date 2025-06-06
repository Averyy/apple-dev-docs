# didOpenNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the drawer is opened.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class let didOpenNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSDrawer` object that opened. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let didCloseNotification: NSNotification.Name](nsdrawer/didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let willCloseNotification: NSNotification.Name](nsdrawer/willclosenotification.md)
  Posted whenever the drawer is about to close.
- [class let willOpenNotification: NSNotification.Name](nsdrawer/willopennotification.md)
  Posted whenever the drawer is about to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/didopennotification)*