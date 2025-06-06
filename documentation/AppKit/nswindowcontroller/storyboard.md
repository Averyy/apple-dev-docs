# storyboard

**Framework**: AppKit  
**Kind**: property

The storyboard file from which the window controller was loaded.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var storyboard: NSStoryboard? { get }
```

#### Discussion

The value of this property is `nil` if the window controller was not loaded from a storyboard.

## See Also

- [var owner: AnyObject?](nswindowcontroller/owner.md)
  The owner of the nib file containing the window managed by the receiver.
- [var windowNibName: NSNib.Name?](nswindowcontroller/windownibname.md)
  The name of the nib file that stores the window associated with the receiver.
- [var windowNibPath: String?](nswindowcontroller/windownibpath.md)
  The full path of the nib file that stores the window associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/storyboard)*