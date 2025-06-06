# deviceCapabilities

**Framework**: Nearby Interaction  
**Kind**: property

A protocol object that describes the nearby interaction capabilities of a person’s device.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- watchOS 10.0+

## Declaration

```swift
@NSCopying
var deviceCapabilities: any NIDeviceCapability { get }
```

## Mentions

- [Extending advanced direction finding and ranging](extending-advanced-direction-finding-and-ranging.md)

#### Discussion

Use the [`NIDeviceCapability`](nidevicecapability.md) instance this property returns to detect the available capabilities on a person’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidiscoverytoken/devicecapabilities)*