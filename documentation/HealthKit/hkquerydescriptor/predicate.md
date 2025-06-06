# predicate

**Framework**: HealthKit  
**Kind**: property

The predicate that filters samples matching this descriptor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@NSCopying
var predicate: NSPredicate? { get }
```

#### Discussion

If the predicate is `nil`, the descriptor matches all samples of the data type specified by the [`sampleType`](hkquerydescriptor/sampletype.md) property.

## See Also

- [var sampleType: HKSampleType](hkquerydescriptor/sampletype.md)
  The data type of samples that match this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquerydescriptor/predicate)*