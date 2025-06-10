# mice()

**Framework**: Game Controller  
**Kind**: method

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

#### Return Value

The currently connected mouse devices.

## See Also

- [static let GCMouseDidConnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCMouseDidConnect.md)
  A notification that posts after a mouse connects to the device.
- [static let GCMouseDidDisconnect: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/GCMouseDidDisconnect.md)
  A notification that posts after a mouse disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/mice())*