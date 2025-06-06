# quantityType(forIdentifier:)

**Framework**: HealthKit  
**Kind**: method

Returns the shared quantity type for the provided identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func quantityType(forIdentifier identifier: HKQuantityTypeIdentifier) -> HKQuantityType?
```

## Mentions

- [Saving data to HealthKit](saving-data-to-healthkit.md)

#### Return Value

The shared `HKQuantityType` instance based on the provided identifier.

#### Discussion

This method returns an instance of the [`HKQuantityType`](hkquantitytype.md) concrete subclass. HealthKit uses quantity types to create samples that store a numerical value. Use quantity type instances to create quantity samples that you can save in the HealthKit store. For more information, see [`HKQuantitySample`](hkquantitysample.md).

## Parameters

- `identifier`: A quantity type identifier. For a list of valid identifiers, see  .

## See Also

- [struct HKQuantityTypeIdentifier](hkquantitytypeidentifier.md)
  The identifiers that create quantity type objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/quantitytype(foridentifier:))*