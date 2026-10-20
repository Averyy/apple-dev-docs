# current

**Framework**: Game Controller  
**Kind**: property  
**Role**: Type Property

The most recent mouse that the user connects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var current: GCMouse? { get }
```

```objc
@property (class, atomic, strong, readonly, nullable) GCMouse * current;
```

## See Also

### Handling multiple mouse devices
- [static let GCMouseDidBecomeCurrent: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gcmousedidbecomecurrent.md)
  A notification that posts when a mouse becomes the most recent mouse that the user connects.
- [static let GCMouseDidStopBeingCurrent: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gcmousedidstopbeingcurrent.md)
  A notification that posts when a mouse stops being the most recent mouse that the user connects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/current)*