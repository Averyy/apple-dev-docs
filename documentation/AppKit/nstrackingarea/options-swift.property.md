# options

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The options specified for the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var options: NSTrackingArea.Options { get }
```

```objc
@property (readonly) NSTrackingAreaOptions options;
```

#### Discussion

The options for an `NSTrackingArea` object are specified when the object is created.

## See Also

### Getting Object Attributes
- [var owner: AnyObject?](./owner.md)
  The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.
- [var rect: NSRect](./rect.md)
  The rectangle defining the area encompassed by the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The dictionary containing the data associated with the receiver when it was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/options-swift.property)*