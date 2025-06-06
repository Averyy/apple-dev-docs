# connectionID

**Framework**: External Accessory  
**Kind**: property

The accessory’s unique ID for connecting to the iOS-based device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var connectionID: Int { get }
```

#### Discussion

The connection ID uniquely identifies this accessory to the device. If multiple accessories of the same type are connected to the device, you can use this information to distinguish between them.

The connection ID for an accessory persists only for the duration of the current connection. If the accessory is disconnected and reconnected, a new connection ID is assigned.

## See Also

- [var isConnected: Bool](eaaccessory/isconnected.md)
  A Boolean value indicating whether the accessory is currently connected to the iOS-based device.
- [Null Connection ID](null-connection-id.md)
  The ID for an unconnected accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessory/connectionid)*