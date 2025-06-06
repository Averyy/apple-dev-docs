# objects(for:)

**Framework**: HealthKit  
**Kind**: method

Returns a set containing all the objects of the specified type in the correlation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func objects(for objectType: HKObjectType) -> Set<HKSample>
```

#### Return Value

A set containing all the objects of the specified type in the correlation.

## Parameters

- `objectType`: The quantity or category type for the data stored inside the correlation. For example, to get all the samples measuring calories from inside a correlation, use an   object created with the   identifier.

## See Also

- [var correlationType: HKCorrelationType](hkcorrelation/correlationtype.md)
  The type for this correlation.
- [var objects: Set<HKSample>](hkcorrelation/objects.md)
  The set of sample objects that make up the correlation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcorrelation/objects(for:))*