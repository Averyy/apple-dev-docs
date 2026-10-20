# connectedRacingWheels

**Framework**: Game Controller  
**Kind**: property  
**Role**: Type Property

The racing wheels connected to the device.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class var connectedRacingWheels: Set<GCRacingWheel> { get }
```

```objc
@property (class, nonatomic, readonly) NSSet<GCRacingWheel *> * connectedRacingWheels;
```

## See Also

### Discovering racing wheels
- [static let GCRacingWheelDidConnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gcracingwheeldidconnect.md)
  A notification that posts after a racing wheel controller connects to the device.
- [static let GCRacingWheelDidDisconnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gcracingwheeldiddisconnect.md)
  A notification that posts after a racing wheel controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/connectedracingwheels)*