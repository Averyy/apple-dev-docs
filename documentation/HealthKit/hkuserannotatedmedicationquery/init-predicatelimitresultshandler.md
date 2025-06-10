# init(predicate:limit:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(predicate: NSPredicate?, limit: Int, resultsHandler: @escaping (HKUserAnnotatedMedicationQuery, HKUserAnnotatedMedication?, Bool, (any Error)?) -> Void)
```

## Parameters

- `predicate`: The predicate which user annotated medications should match.
- `limit`: The maximum number of  user annotated medications to return.  Pass HKObjectQueryNoLimit for no limit.
- `resultsHandler`: The block to invoke with results to deliver to the client. The results handler will be called with done = YES when there are no more user annotated medications to enumerate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedicationquery/init(predicate:limit:resultshandler:))*