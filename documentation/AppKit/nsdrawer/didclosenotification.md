# didCloseNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the drawer is closed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class let didCloseNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSDrawer` object that closed. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let didOpenNotification: NSNotification.Name](nsdrawer/didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willCloseNotification: NSNotification.Name](nsdrawer/willclosenotification.md)
  Posted whenever the drawer is about to close.
- [class let willOpenNotification: NSNotification.Name](nsdrawer/willopennotification.md)
  Posted whenever the drawer is about to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/didclosenotification)*