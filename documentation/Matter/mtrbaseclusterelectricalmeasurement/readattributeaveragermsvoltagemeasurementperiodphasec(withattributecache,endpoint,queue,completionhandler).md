# readAttributeAverageRmsVoltageMeasurementPeriodPhaseC(withAttributeCache:endpoint:queue:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use readAttributeAverageRmsVoltageMeasurementPeriodPhaseCWithAttributeCache:endpoint:queue:completion:

## Declaration

```swift
class func readAttributeAverageRmsVoltageMeasurementPeriodPhaseC(withAttributeCache attributeCacheContainer: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: @escaping @Sendable (NSNumber?, (any Error)?) -> Void)
```

```swift
class func readAttributeAverageRmsVoltageMeasurementPeriodPhaseC(withAttributeCache attributeCacheContainer: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> NSNumber
```

```objc
+ (void) readAttributeAverageRmsVoltageMeasurementPeriodPhaseCWithAttributeCache:(MTRAttributeCacheContainer *) attributeCacheContainer endpoint:(NSNumber *) endpoint queue:(dispatch_queue_t) queue completionHandler:(void (^)(NSNumber *value, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterelectricalmeasurement/readattributeaveragermsvoltagemeasurementperiodphasec(withattributecache:endpoint:queue:completionhandler:))*