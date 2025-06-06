# deviceController(_:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:)

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
func deviceController(_ controller: UUID, nodeID: NSNumber, readAttributeWithEndpointID endpointID: NSNumber, clusterID: NSNumber, attributeID: NSNumber, params: MTRReadParams?) async -> [String : Any]?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice/devicecontroller(_:nodeid:readattributewithendpointid:clusterid:attributeid:params:withreply:))*