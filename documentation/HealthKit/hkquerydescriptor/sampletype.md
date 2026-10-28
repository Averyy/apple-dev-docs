# sampleType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The data type of samples that match this descriptor.

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
var sampleType: HKSampleType { get }
```

```objc
@property (nonatomic, copy, readonly) HKSampleType * sampleType;
```

## Discussion

For more information, see [Data types](../data-types.md).

## See Also

### Accessing Descriptor Data
- [var predicate: NSPredicate?](./predicate.md)
  The predicate that filters samples matching this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquerydescriptor/sampletype)*