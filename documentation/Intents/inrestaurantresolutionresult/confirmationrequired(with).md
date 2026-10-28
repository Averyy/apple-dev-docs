# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func confirmationRequired(with restaurantToConfirm: INRestaurant?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithRestaurantToConfirm:(INRestaurant *) restaurantToConfirm;
```

## Return Value

A new [`INRestaurantResolutionResult`](../inrestaurantresolutionresult.md) object.

## Discussion

Use this method when you can resolve the restaurant to a known establishment but you want the user to confirm that value before proceeding. You might ask for confirmation when there is some doubt that the specified restaurant is what the user intended.

## Parameters

- `restaurantToConfirm`: The restaurant for the user to confirm.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INRestaurant) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INRestaurant]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantresolutionresult/confirmationrequired(with:))*