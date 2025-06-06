# subscribeAttribute(withController:nodeId:endpointId:clusterId:attributeId:minInterval:maxInterval:params:establishedHandler:)

**Framework**: Matter  
**Kind**: method  
**Required**: Yes

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
func subscribeAttribute(withController controller: Any?, nodeId: UInt64, endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, minInterval: NSNumber, maxInterval: NSNumber, params: [String : Any]?, establishedHandler: @escaping () -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerserverprotocol/subscribeattribute(withcontroller:nodeid:endpointid:clusterid:attributeid:mininterval:maxinterval:params:establishedhandler:))*