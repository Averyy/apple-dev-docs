# subscribeAttribute(withEndpointId:clusterId:attributeId:minInterval:maxInterval:params:clientQueue:reportHandler:subscriptionEstablished:)

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
func subscribeAttribute(withEndpointId endpointId: NSNumber?, clusterId: NSNumber?, attributeId: NSNumber?, minInterval: NSNumber, maxInterval: NSNumber, params: MTRSubscribeParams?, clientQueue: dispatch_queue_t, reportHandler: @escaping MTRDeviceResponseHandler, subscriptionEstablished subscriptionEstablishedHandler: (() -> Void)? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/subscribeattribute(withendpointid:clusterid:attributeid:mininterval:maxinterval:params:clientqueue:reporthandler:subscriptionestablished:))*