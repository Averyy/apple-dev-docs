# willCloseNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever the drawer is about to close.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class let willCloseNotification: NSNotification.Name
```

#### Discussion

The notification object is the `NSDrawer`object about to close. This notification does not contain a `userInfo` dictionary.

## See Also

- [class let didCloseNotification: NSNotification.Name](nsdrawer/didclosenotification.md)
  Posted whenever the drawer is closed.
- [class let didOpenNotification: NSNotification.Name](nsdrawer/didopennotification.md)
  Posted whenever the drawer is opened.
- [class let willOpenNotification: NSNotification.Name](nsdrawer/willopennotification.md)
  Posted whenever the drawer is about to open.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/willclosenotification)*