# correlationType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The type for this correlation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var correlationType: HKCorrelationType { get }
```

```objc
@property (readonly) HKCorrelationType * correlationType;
```

#### Discussion

For a complete list of correlation type identifiers, see [`HKCorrelationTypeIdentifier`](../hkcorrelationtypeidentifier.md).

## See Also

### Getting Correlation Data
- [var objects: Set<HKSample>](./objects.md)
  The set of sample objects that make up the correlation.
- [func objects(for: HKObjectType) -> Set<HKSample>](./objects%28for%29.md)
  Returns a set containing all the objects of the specified type in the correlation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelation/correlationtype)*