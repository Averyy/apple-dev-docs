# restaurant

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The restaurant to use when determining any default values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var restaurant: INRestaurant? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INRestaurant * restaurant;
```

*macOS*

```objc
@property (atomic, copy, nullable) INRestaurant * restaurant;
```

#### Discussion

Use the specified restaurant to identify any restaurant-related requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintent/restaurant)*