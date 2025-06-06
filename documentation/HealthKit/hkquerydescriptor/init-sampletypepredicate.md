# init(sampleType:predicate:)

**Framework**: HealthKit  
**Kind**: init

Creates a new descriptor for the data type and predicate you provided.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(sampleType: HKSampleType, predicate: NSPredicate?)
```

## Parameters

- `sampleType`: The data type of samples that match this descriptor. For more information, see  .
- `predicate`: The predicate used to filter samples that match this descriptor. If the predicate is  , the descriptor matches all samples of the specified data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquerydescriptor/init(sampletype:predicate:))*