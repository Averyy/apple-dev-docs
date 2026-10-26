# init(restaurant:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified restaurant.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(restaurant: INRestaurant?)
```

```objc
- (instancetype) initWithRestaurant:(INRestaurant *) restaurant;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when Maps asks for the default information to use when booking the restaurant. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `restaurant`: The restaurant associated with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintent/init(restaurant:))*