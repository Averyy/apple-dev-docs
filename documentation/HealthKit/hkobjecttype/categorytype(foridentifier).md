# categoryType(forIdentifier:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns the shared category type for the provided identifier.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
class func categoryType(forIdentifier identifier: HKCategoryTypeIdentifier) -> HKCategoryType?
```

```objc
+ (HKCategoryType *) categoryTypeForIdentifier:(HKCategoryTypeIdentifier) identifier;
```

## Return Value

The shared `HKCategoryType` instance based on the provided identifier.

## Discussion

This method returns an instance of the [`HKCategoryType`](../hkcategorytype.md) concrete subclass. HealthKit uses category types to represent data that can be categorized into an enumeration of values. Use category type instances to create category samples that you can then save in the HealthKit store. For more information, see [`HKCategorySample`](../hkcategorysample.md).

## Parameters

- `identifier`: A category type identifier. For a list of valid identifiers, see [`HKCategoryTypeIdentifier`](../hkcategorytypeidentifier.md).

## See Also

### Creating category types
- [struct HKCategoryTypeIdentifier](../hkcategorytypeidentifier.md)
  Identifiers for creating category types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/categorytype(foridentifier:))*