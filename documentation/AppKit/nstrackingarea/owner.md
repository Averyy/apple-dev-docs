# owner

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.

**Availability**:
- macOS 10.5+

## Declaration

```swift
weak var owner: AnyObject? { get }
```

```objc
@property (weak, readonly, nullable) id owner;
```

## See Also

### Getting Object Attributes
- [var options: NSTrackingArea.Options](./options-swift.property.md)
  The options specified for the receiver.
- [var rect: NSRect](./rect.md)
  The rectangle defining the area encompassed by the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The dictionary containing the data associated with the receiver when it was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/owner)*