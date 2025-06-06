# windowNibPath

**Framework**: AppKit  
**Kind**: property

The full path of the nib file that stores the window associated with the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windowNibPath: String? { get }
```

#### Discussion

If [`init(windowNibPath:owner:)`](nswindowcontroller/init(windownibpath:owner:).md) was used to initialize the instance, this property contains the path. If [`init(windowNibName:)`](nswindowcontroller/init(windownibname:).md) or [`init(windowNibName:owner:)`](nswindowcontroller/init(windownibname:owner:).md) was used, [`windowNibPath`](nswindowcontroller/windownibpath.md) locates the nib in the file’s owner’s class’ bundle or in the application’s main bundle and returns the full path (or `nil` if it cannot be located). Subclasses can override this behavior to augment the search behavior, but probably ought to call `super` first.

## See Also

- [var owner: AnyObject?](nswindowcontroller/owner.md)
  The owner of the nib file containing the window managed by the receiver.
- [var storyboard: NSStoryboard?](nswindowcontroller/storyboard.md)
  The storyboard file from which the window controller was loaded.
- [var windowNibName: NSNib.Name?](nswindowcontroller/windownibname.md)
  The name of the nib file that stores the window associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windownibpath)*