# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func disambiguation(with placemarksToDisambiguate: [CLPlacemark]) -> Self
```

```objc
+ (instancetype) disambiguationWithPlacemarksToDisambiguate:(NSArray<CLPlacemark *> *) placemarksToDisambiguate;
```

#### Return Value

A new [`INPlacemarkResolutionResult`](../inplacemarkresolutionresult.md) object.

#### Discussion

Use this method to create a result object when there is more one value that might match the given parameter. The user is asked to select from among the objects you provide.

## Parameters

- `placemarksToDisambiguate`: An array of [`CLPlacemark`](../../CoreLocation/clplacemark.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: CLPlacemark) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: CLPlacemark?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplacemarkresolutionresult/disambiguation(with:))*