# categoryType(forIdentifier:)

**Framework**: HealthKit  
**Kind**: method

Returns the shared category type for the provided identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func categoryType(forIdentifier identifier: HKCategoryTypeIdentifier) -> HKCategoryType?
```

#### Return Value

The shared `HKCategoryType` instance based on the provided identifier.

#### Discussion

This method returns an instance of the [`HKCategoryType`](hkcategorytype.md) concrete subclass. HealthKit uses category types to represent data that can be categorized into an enumeration of values. Use category type instances to create category samples that you can then save in the HealthKit store. For more information, see [`HKCategorySample`](hkcategorysample.md).

## Parameters

- `identifier`: A category type identifier. For a list of valid identifiers, see  .

## See Also

- [struct HKCategoryTypeIdentifier](hkcategorytypeidentifier.md)
  Identifiers for creating category types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/categorytype(foridentifier:))*