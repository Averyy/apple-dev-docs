# subscribe(with:params:clusterStateCacheContainer:attributeReportHandler:eventReportHandler:errorHandler:subscriptionEstablished:resubscriptionScheduled:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func subscribe(with queue: dispatch_queue_t, params: MTRSubscribeParams, clusterStateCacheContainer: MTRClusterStateCacheContainer?, attributeReportHandler: MTRDeviceReportHandler?, eventReportHandler: MTRDeviceReportHandler?, errorHandler: @escaping MTRDeviceErrorHandler, subscriptionEstablished: MTRSubscriptionEstablishedHandler?, resubscriptionScheduled: MTRDeviceResubscriptionScheduledHandler? = nil)
```

```objc
- (void) subscribeWithQueue:(dispatch_queue_t) queue params:(MTRSubscribeParams *) params clusterStateCacheContainer:(MTRClusterStateCacheContainer *) clusterStateCacheContainer attributeReportHandler:(MTRDeviceReportHandler) attributeReportHandler eventReportHandler:(MTRDeviceReportHandler) eventReportHandler errorHandler:(MTRDeviceErrorHandler) errorHandler subscriptionEstablished:(MTRSubscriptionEstablishedHandler) subscriptionEstablished resubscriptionScheduled:(MTRDeviceResubscriptionScheduledHandler) resubscriptionScheduled;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/subscribe(with:params:clusterstatecachecontainer:attributereporthandler:eventreporthandler:errorhandler:subscriptionestablished:resubscriptionscheduled:))*