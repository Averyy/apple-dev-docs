# subscribeAttribute(withEndpointId:clusterId:attributeId:minInterval:maxInterval:params:clientQueue:reportHandler:subscriptionEstablished:)

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

> **Deprecated**: Please use subscribeToAttributesWithEndpointID:clusterID:attributeID:params:queue:reportHandler:subscriptionEstablished:

## Declaration

```swift
func subscribeAttribute(withEndpointId endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, minInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, clientQueue: dispatch_queue_t, reportHandler: @escaping MTRDeviceResponseHandler, subscriptionEstablished subscriptionEstablishedHandler: (() -> Void)? = nil)
```

```objc
- (void) subscribeAttributeWithEndpointId:(NSNumber *) endpointId clusterId:(NSNumber *) clusterId attributeId:(NSNumber *) attributeId minInterval:(NSNumber *) minInterval maxInterval:(NSNumber *) maxInterval params:(MTRSubscribeParams *) params clientQueue:(dispatch_queue_t) clientQueue reportHandler:(MTRDeviceResponseHandler) reportHandler subscriptionEstablished:(dispatch_block_t) subscriptionEstablishedHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/subscribeattribute(withendpointid:clusterid:attributeid:mininterval:maxinterval:params:clientqueue:reporthandler:subscriptionestablished:))*