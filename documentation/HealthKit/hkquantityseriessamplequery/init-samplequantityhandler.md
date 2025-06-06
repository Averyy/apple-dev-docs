# init(sample:quantityHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a new series query.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(sample quantitySample: HKQuantitySample, quantityHandler: @escaping (HKQuantitySeriesSampleQuery, HKQuantity?, Date?, Bool, (any Error)?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequery/init(sample:quantityhandler:))*