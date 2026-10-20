# readAttribute(withEndpointId:clusterId:attributeId:params:clientQueue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use readAttributesWithEndpointID:clusterID:attributeID:params:queue:completion:

## Declaration

```swift
func readAttribute(withEndpointId endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, params: MTRReadParams?, clientQueue: dispatch_queue_t, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func readAttribute(withEndpointId endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, params: MTRReadParams?, clientQueue: dispatch_queue_t) async throws -> [[String : Any]]
```

```objc
- (void) readAttributeWithEndpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId attributeId:(NSNumber *) attributeId params:(MTRReadParams *) params clientQueue:(dispatch_queue_t) clientQueue completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/readattribute(withendpointid:clusterid:attributeid:params:clientqueue:completion:))*