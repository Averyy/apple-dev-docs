# subscribe(with:minInterval:maxInterval:params:cacheContainer:attributeReportHandler:eventReportHandler:errorHandler:subscriptionEstablished:resubscriptionScheduled:)

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

> **Deprecated**: Please use subscribeWithQueue:params:clusterStateCacheContainer:attributeReportHandler:eventReportHandler:errorHandler:subscriptionEstablished:resubscriptionScheduled:

## Declaration

```swift
func subscribe(with queue: dispatch_queue_t, minInterval: UInt16, maxInterval: UInt16, params: MTRSubscribeParams?, cacheContainer attributeCacheContainer: MTRAttributeCacheContainer?, attributeReportHandler: MTRDeviceReportHandler?, eventReportHandler: MTRDeviceReportHandler?, errorHandler: @escaping MTRDeviceErrorHandler, subscriptionEstablished subscriptionEstablishedHandler: (() -> Void)?, resubscriptionScheduled resubscriptionScheduledHandler: MTRDeviceResubscriptionScheduledHandler? = nil)
```

```objc
- (void) subscribeWithQueue:(dispatch_queue_t) queue minInterval:(uint16_t) minInterval maxInterval:(uint16_t) maxInterval params:(MTRSubscribeParams *) params cacheContainer:(MTRAttributeCacheContainer *) attributeCacheContainer attributeReportHandler:(MTRDeviceReportHandler) attributeReportHandler eventReportHandler:(MTRDeviceReportHandler) eventReportHandler errorHandler:(MTRDeviceErrorHandler) errorHandler subscriptionEstablished:(dispatch_block_t) subscriptionEstablishedHandler resubscriptionScheduled:(MTRDeviceResubscriptionScheduledHandler) resubscriptionScheduledHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/subscribe(with:mininterval:maxinterval:params:cachecontainer:attributereporthandler:eventreporthandler:errorhandler:subscriptionestablished:resubscriptionscheduled:))*