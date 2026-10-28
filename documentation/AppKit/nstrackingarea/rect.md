# rect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle defining the area encompassed by the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var rect: NSRect { get }
```

```objc
@property (readonly) NSRect rect;
```

## Discussion

The rectangle is specified in the local coordinate system of the associated view. If the [`inVisibleRect`](./options-swift.struct/invisiblerect.md) option is specified, the receiver is automatically synchronized with changes in the view’s visible area ([`visibleRect`](../nsview/visiblerect.md)) and the value of this property is ignored.

## See Also

### Getting Object Attributes
- [var options: NSTrackingArea.Options](./options-swift.property.md)
  The options specified for the receiver.
- [var owner: AnyObject?](./owner.md)
  The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The dictionary containing the data associated with the receiver when it was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/rect)*