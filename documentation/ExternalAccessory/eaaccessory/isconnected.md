# isConnected

**Framework**: External Accessory  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the accessory is currently connected to the iOS-based device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isConnected: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isConnected) BOOL connected;
```

## See Also

### Getting Connection Information
- [var connectionID: Int](./connectionid.md)
  The accessory’s unique ID for connecting to the iOS-based device.
- [Null Connection ID](../null-connection-id.md)
  The ID for an unconnected accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eaaccessory/isconnected)*