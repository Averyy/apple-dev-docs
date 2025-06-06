# userInfo

**Framework**: AppKit  
**Kind**: property

The dictionary containing the data associated with the receiver when it was created.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get }
```

#### Discussion

You can obtain this dictionary per event in each [`mouseEntered(with:)`](nsresponder/mouseentered(with:).md) and [`mouseExited(with:)`](nsresponder/mouseexited(with:).md) method by querying the passed-in `NSEvent` object with `[[event trackingArea] userData]`.

## See Also

- [var options: NSTrackingArea.Options](nstrackingarea/options-swift.property.md)
  The options specified for the receiver.
- [var owner: AnyObject?](nstrackingarea/owner.md)
  The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.
- [var rect: NSRect](nstrackingarea/rect.md)
  The rectangle defining the area encompassed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/userinfo)*