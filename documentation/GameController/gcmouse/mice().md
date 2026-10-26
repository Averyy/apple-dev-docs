# mice()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Type Method

Returns any mice that the user connects to the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func mice() -> [GCMouse]
```

```objc
+ (NSArray<GCMouse *> *) mice;
```

#### Return Value

The currently connected mouse devices.

## See Also

### Discovering mouse devices
- [static let GCMouseDidConnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gcmousedidconnect.md)
  A notification that posts after a mouse connects to the device.
- [static let GCMouseDidDisconnect: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gcmousediddisconnect.md)
  A notification that posts after a mouse disconnects from the device.
- [GCMouseDidConnectNotification](../gcmousedidconnectnotification.md)
  A notification that posts after a mouse connects to the device.
- [GCMouseDidDisconnectNotification](../gcmousediddisconnectnotification.md)
  A notification that posts after a mouse disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/mice())*