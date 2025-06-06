# subscribe(with:minInterval:maxInterval:params:cacheContainer:attributeReportHandler:eventReportHandler:errorHandler:subscriptionEstablished:resubscriptionScheduled:)

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
func subscribe(with queue: dispatch_queue_t, minInterval: UInt16, maxInterval: UInt16, params: MTRSubscribeParams?, cacheContainer attributeCacheContainer: MTRAttributeCacheContainer?, attributeReportHandler: MTRDeviceReportHandler?, eventReportHandler: MTRDeviceReportHandler?, errorHandler: @escaping MTRDeviceErrorHandler, subscriptionEstablished subscriptionEstablishedHandler: (() -> Void)?, resubscriptionScheduled resubscriptionScheduledHandler: MTRDeviceResubscriptionScheduledHandler? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/subscribe(with:mininterval:maxinterval:params:cachecontainer:attributereporthandler:eventreporthandler:errorhandler:subscriptionestablished:resubscriptionscheduled:))*