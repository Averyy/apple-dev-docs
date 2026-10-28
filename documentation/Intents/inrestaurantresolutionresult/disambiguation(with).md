# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func disambiguation(with restaurantsToDisambiguate: [INRestaurant]) -> Self
```

```objc
+ (instancetype) disambiguationWithRestaurantsToDisambiguate:(NSArray<INRestaurant *> *) restaurantsToDisambiguate;
```

## Return Value

A new [`INRestaurantResolutionResult`](../inrestaurantresolutionresult.md) object.

## Discussion

Use this method when you cannot resolve the restaurant uniquely and need the user to select from a limited set of possible values.

## Parameters

- `restaurantsToDisambiguate`: An array of restaurants from which to select. Specify as few items as possible, and preferably no more than five.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INRestaurant) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INRestaurant?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantresolutionresult/disambiguation(with:))*