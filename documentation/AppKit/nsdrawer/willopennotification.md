# willOpenNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the drawer is about to open.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class let willOpenNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSDrawer` object about to open. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let didCloseNotification: NSNotification.Name](nsdrawer/didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let didOpenNotification: NSNotification.Name](nsdrawer/didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willCloseNotification: NSNotification.Name](nsdrawer/willclosenotification.md)
  Posted whenever the drawer is about to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/willopennotification)*