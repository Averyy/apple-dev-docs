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
class func disambiguation(with restaurantGuestsToDisambiguate: [INRestaurantGuest]) -> Self
```

```objc
+ (instancetype) disambiguationWithRestaurantGuestsToDisambiguate:(NSArray<INRestaurantGuest *> *) restaurantGuestsToDisambiguate;
```

#### Return Value

A new [`INRestaurantGuestResolutionResult`](../inrestaurantguestresolutionresult.md) object.

#### Discussion

Use this method when you cannot resolve the guest uniquely and need the user to select from a limited set of possible guests.

## Parameters

- `restaurantGuestsToDisambiguate`: An array of [`INRestaurantGuest`](../inrestaurantguest.md) objects from which to select. Specify as few items as possible, and preferably no more than five.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INRestaurantGuest) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INRestaurantGuest?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestresolutionresult/disambiguation(with:))*