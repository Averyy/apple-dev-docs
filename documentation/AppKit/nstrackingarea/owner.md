# owner

**Framework**: AppKit  
**Kind**: property

The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.

**Availability**:
- macOS 10.5+

## Declaration

```swift
weak var owner: AnyObject? { get }
```

## See Also

- [var options: NSTrackingArea.Options](nstrackingarea/options-swift.property.md)
  The options specified for the receiver.
- [var rect: NSRect](nstrackingarea/rect.md)
  The rectangle defining the area encompassed by the receiver.
- [var userInfo: [AnyHashable : Any]?](nstrackingarea/userinfo.md)
  The dictionary containing the data associated with the receiver when it was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/owner)*