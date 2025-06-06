# owner

**Framework**: AppKit  
**Kind**: property

The owner of the nib file containing the window managed by the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var owner: AnyObject? { get }
```

#### Discussion

The owner of the nib file containing the window managed by the receiver is usually `self`, but it can be the receiver’s document or some other object.

## See Also

- [var storyboard: NSStoryboard?](nswindowcontroller/storyboard.md)
  The storyboard file from which the window controller was loaded.
- [var windowNibName: NSNib.Name?](nswindowcontroller/windownibname.md)
  The name of the nib file that stores the window associated with the receiver.
- [var windowNibPath: String?](nswindowcontroller/windownibpath.md)
  The full path of the nib file that stores the window associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/owner)*