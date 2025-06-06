# subscribeToAttributes(withEndpointID:clusterID:attributeID:params:queue:reportHandler:subscriptionEstablished:)

**Framework**: Matter  
**Kind**: method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func subscribeToAttributes(withEndpointID endpointID: NSNumber?, clusterID: NSNumber?, attributeID: NSNumber?, params: MTRSubscribeParams?, queue: dispatch_queue_t, reportHandler: @escaping MTRDeviceResponseHandler, subscriptionEstablished: MTRSubscriptionEstablishedHandler? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/subscribetoattributes(withendpointid:clusterid:attributeid:params:queue:reporthandler:subscriptionestablished:))*