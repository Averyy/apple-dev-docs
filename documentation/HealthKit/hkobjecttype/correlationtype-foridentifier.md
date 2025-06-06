# correlationType(forIdentifier:)

**Framework**: HealthKit  
**Kind**: method

Returns the shared correlation type for the provided identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func correlationType(forIdentifier identifier: HKCorrelationTypeIdentifier) -> HKCorrelationType?
```

#### Return Value

The shared [`HKCorrelationType`](hkcorrelationtype.md) instance based on the provided identifier.

#### Discussion

This method returns an instance of the [`HKCorrelationType`](hkcorrelationtype.md) concrete subclass. HealthKit uses correlation types to create complex data objects that contain multiple values. Use correlation type instances to create correlation objects that you can save in the HealthKit store. For more information, see [`HKCorrelation`](hkcorrelation.md).

## Parameters

- `identifier`: A correlation type identifier. For a list of valid identifiers, see  .

## See Also

- [struct HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier.md)
  The identifiers that create correlation type objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/correlationtype(foridentifier:))*