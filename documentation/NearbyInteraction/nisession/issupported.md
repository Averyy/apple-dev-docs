# isSupported

**Framework**: Nearby Interaction  
**Kind**: property

A Boolean value that indicates whether the device supports basic interaction-session functionality.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
class var isSupported: Bool { get }
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

> ⚠️ **Warning**:  This property is deprecated.

##### Check the Devices Supported Features

In iOS 16 and watchOS 9, check a device’s supported features with [`deviceCapabilities`](nisession/devicecapabilities.md) instead of calling this function.

The value of the [`supportsPreciseDistanceMeasurement`](nidevicecapability/supportsprecisedistancemeasurement.md) device capability is equivalent to this property, as demonstrated in the following code.

```swift
var isSupported : Bool
if #available(iOS 16.0, watchOS 9.0, *) {
    isSupported = NISession.deviceCapabilities.supportsPreciseDistanceMeasurement
} else {
    isSupported = NISession.isSupported
}
if isSupported {
    // Initiate a nearby interaction session.
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/issupported)*