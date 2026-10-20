# windowNibName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the nib file that stores the window associated with the receiver.

**Availability**:
- macOS

## Declaration

```swift
var windowNibName: NSNib.Name? { get }
```

```objc
@property (copy, readonly, nullable) NSNibName windowNibName;
```

#### Discussion

If [`init(windowNibPath:owner:)`](./init%28windownibpath,owner%29.md) was used to initialize the instance, [`windowNibName`](./windownibname.md) contains the last path component with the “`.nib`” extension stripped off. If [`init(windowNibName:)`](./init%28windownibname%29.md) or [`init(windowNibName:owner:)`](./init%28windownibname,owner%29.md) was used, [`NSWindowController`](../nswindowcontroller.md) contains the name without the “`.nib`” extension.

## See Also

### Getting Nib and Storyboard Information
- [var owner: AnyObject?](./owner.md)
  The owner of the nib file containing the window managed by the receiver.
- [var storyboard: NSStoryboard?](./storyboard.md)
  The storyboard file from which the window controller was loaded.
- [var windowNibPath: String?](./windownibpath.md)
  The full path of the nib file that stores the window associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windownibname)*