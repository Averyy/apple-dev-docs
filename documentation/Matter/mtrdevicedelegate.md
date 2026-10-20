# MTRDeviceDelegate

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MTRDeviceDelegate <NSObject>
```

## Topics

### Instance Methods
- [func device(MTRDevice, receivedAttributeReport: [[String : Any]])](./mtrdevicedelegate/device%28_,receivedattributereport%29.md)
- [func device(MTRDevice, receivedEventReport: [[String : Any]])](./mtrdevicedelegate/device%28_,receivedeventreport%29.md)
- [func device(MTRDevice, stateChanged: MTRDeviceState)](./mtrdevicedelegate/device%28_,statechanged%29.md)
- [func deviceBecameActive(MTRDevice)](./mtrdevicedelegate/devicebecameactive%28_%29.md)
- [func deviceCachePrimed(MTRDevice)](./mtrdevicedelegate/devicecacheprimed%28_%29.md)
- [func deviceConfigurationChanged(MTRDevice)](./mtrdevicedelegate/deviceconfigurationchanged%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicedelegate)*