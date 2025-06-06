# MTRDeviceDelegate

**Framework**: Matter  
**Kind**: protocol

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol MTRDeviceDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func device(MTRDevice, receivedAttributeReport: [[String : Any]])](mtrdevicedelegate/device(_:receivedattributereport:).md)
- [func device(MTRDevice, receivedEventReport: [[String : Any]])](mtrdevicedelegate/device(_:receivedeventreport:).md)
- [func device(MTRDevice, stateChanged: MTRDeviceState)](mtrdevicedelegate/device(_:statechanged:).md)
- [func deviceBecameActive(MTRDevice)](mtrdevicedelegate/devicebecameactive(_:).md)
- [func deviceCachePrimed(MTRDevice)](mtrdevicedelegate/devicecacheprimed(_:).md)
- [func deviceConfigurationChanged(MTRDevice)](mtrdevicedelegate/deviceconfigurationchanged(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicedelegate)*