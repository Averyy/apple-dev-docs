# owner

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The owner of the nib file containing the window managed by the receiver.

**Availability**:
- macOS

## Declaration

```swift
weak var owner: AnyObject? { get }
```

```objc
@property (weak, readonly) id owner;
```

#### Discussion

The owner of the nib file containing the window managed by the receiver is usually `self`, but it can be the receiver’s document or some other object.

## See Also

### Getting Nib and Storyboard Information
- [var storyboard: NSStoryboard?](./storyboard.md)
  The storyboard file from which the window controller was loaded.
- [var windowNibName: NSNib.Name?](./windownibname.md)
  The name of the nib file that stores the window associated with the receiver.
- [var windowNibPath: String?](./windownibpath.md)
  The full path of the nib file that stores the window associated with the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/owner)*