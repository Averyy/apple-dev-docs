# init(sample:quantityHandler:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Creates a new series query.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 5.0+ - Deprecated in 6.0

> **Deprecated**: Use [`init(quantityType:predicate:quantityHandler:)`](./init%28quantitytype,predicate,quantityhandler%29.md) instead.

## Declaration

```swift
init(sample quantitySample: HKQuantitySample, quantityHandler: @escaping @Sendable (HKQuantitySeriesSampleQuery, HKQuantity?, Date?, Bool, (any Error)?) -> Void)
```

```objc
- (instancetype) initWithSample:(HKQuantitySample *) quantitySample quantityHandler:(void (^)(HKQuantitySeriesSampleQuery *query, HKQuantity *quantity, NSDate *date, BOOL done, NSError *error)) quantityHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequery/init(sample:quantityhandler:))*