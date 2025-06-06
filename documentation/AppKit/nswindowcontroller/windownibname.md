# windowNibName

**Framework**: AppKit  
**Kind**: property

The name of the nib file that stores the window associated with the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windowNibName: NSNib.Name? { get }
```

#### Discussion

If [`init(windowNibPath:owner:)`](nswindowcontroller/init(windownibpath:owner:).md) was used to initialize the instance, [`windowNibName`](nswindowcontroller/windownibname.md) contains the last path component with the “`.nib`” extension stripped off. If [`init(windowNibName:)`](nswindowcontroller/init(windownibname:).md) or [`init(windowNibName:owner:)`](nswindowcontroller/init(windownibname:owner:).md) was used, [`NSWindowController`](nswindowcontroller.md) contains the name without the “`.nib`” extension.

## See Also

- [var owner: AnyObject?](nswindowcontroller/owner.md)
  The owner of the nib file containing the window managed by the receiver.
- [var storyboard: NSStoryboard?](nswindowcontroller/storyboard.md)
  The storyboard file from which the window controller was loaded.
- [var windowNibPath: String?](nswindowcontroller/windownibpath.md)
  The full path of the nib file that stores the window associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windownibname)*