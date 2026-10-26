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
class func confirmationRequired(with restaurantGuestToConfirm: INRestaurantGuest?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithRestaurantGuestToConfirm:(INRestaurantGuest *) restaurantGuestToConfirm;
```

#### Return Value

A new [`INRestaurantGuestResolutionResult`](../inrestaurantguestresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the guest to a single user of your app, but you want the user to confirm that value before proceeding. You might ask for confirmation when there is some doubt that the specified guest is who the user intended.

## Parameters

- `restaurantGuestToConfirm`: The guest identity for the user to confirm.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INRestaurantGuest) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INRestaurantGuest]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantguestresolutionresult/confirmationrequired(with:))*