# windowNibPath

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The full path of the nib file that stores the window associated with the receiver.

**Availability**:
- macOS

## Declaration

```swift
var windowNibPath: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * windowNibPath;
```

## Discussion

If [`init(windowNibPath:owner:)`](./init%28windownibpath,owner%29.md) was used to initialize the instance, this property contains the path. If [`init(windowNibName:)`](./init%28windownibname%29.md) or [`init(windowNibName:owner:)`](./init%28windownibname,owner%29.md) was used, [`windowNibPath`](./windownibpath.md) locates the nib in the file’s owner’s class’ bundle or in the application’s main bundle and returns the full path (or `nil` if it cannot be located). Subclasses can override this behavior to augment the search behavior, but probably ought to call `super` first.

## See Also

### Getting Nib and Storyboard Information
- [var owner: AnyObject?](./owner.md)
  The owner of the nib file containing the window managed by the receiver.
- [var storyboard: NSStoryboard?](./storyboard.md)
  The storyboard file from which the window controller was loaded.
- [var windowNibName: NSNib.Name?](./windownibname.md)
  The name of the nib file that stores the window associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windownibpath)*