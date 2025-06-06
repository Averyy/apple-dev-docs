# rect

**Framework**: AppKit  
**Kind**: property

The rectangle defining the area encompassed by the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var rect: NSRect { get }
```

#### Discussion

The rectangle is specified in the local coordinate system of the associated view. If the [`inVisibleRect`](nstrackingarea/options-swift.struct/invisiblerect.md) option is specified, the receiver is automatically synchronized with changes in the view’s visible area ([`visibleRect`](nsview/visiblerect.md)) and the value of this property is ignored.

## See Also

- [var options: NSTrackingArea.Options](nstrackingarea/options-swift.property.md)
  The options specified for the receiver.
- [var owner: AnyObject?](nstrackingarea/owner.md)
  The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.
- [var userInfo: [AnyHashable : Any]?](nstrackingarea/userinfo.md)
  The dictionary containing the data associated with the receiver when it was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/rect)*