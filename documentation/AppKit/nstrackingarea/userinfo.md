# userInfo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The dictionary containing the data associated with the receiver when it was created.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var userInfo: [AnyHashable : Any]? { get }
```

```objc
@property (copy, readonly, nullable) NSDictionary<id,id> * userInfo;
```

## Discussion

You can obtain this dictionary per event in each [`mouseEntered(with:)`](../nsresponder/mouseentered%28with%29.md) and [`mouseExited(with:)`](../nsresponder/mouseexited%28with%29.md) method by querying the passed-in `NSEvent` object with `[[event trackingArea] userData]`.

## See Also

### Getting Object Attributes
- [var options: NSTrackingArea.Options](./options-swift.property.md)
  The options specified for the receiver.
- [var owner: AnyObject?](./owner.md)
  The object owning the receiver, which is the recipient of mouse-tracking, mouse-movement, and cursor-update messages.
- [var rect: NSRect](./rect.md)
  The rectangle defining the area encompassed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingarea/userinfo)*