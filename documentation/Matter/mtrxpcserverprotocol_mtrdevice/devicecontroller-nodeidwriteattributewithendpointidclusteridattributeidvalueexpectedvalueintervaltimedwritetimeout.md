# deviceController(_:nodeID:writeAttributeWithEndpointID:clusterID:attributeID:value:expectedValueInterval:timedWriteTimeout:)

**Framework**: Matter  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func deviceController(_ controller: UUID, nodeID: NSNumber, writeAttributeWithEndpointID endpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, value: Any, expectedValueInterval: NSNumber?, timedWriteTimeout timeout: NSNumber?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:writeattributewithendpointid:clusterid:attributeid:value:expectedvalueinterval:timedwritetimeout:))*