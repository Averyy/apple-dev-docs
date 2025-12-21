# readAttribute(withEndpointId:clusterId:attributeId:clientQueue:completion:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
func readAttribute(withEndpointId endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, clientQueue: dispatch_queue_t) async throws -> [[String : Any]]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrattributecachecontainer/readattribute(withendpointid:clusterid:attributeid:clientqueue:completion:))*