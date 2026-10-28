# restaurantIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var restaurantIdentifier: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * restaurantIdentifier;
```

*macOS*

```objc
@property (atomic, copy) NSString * restaurantIdentifier;
```

## Discussion

You provide Apple with unique identifiers for the restaurants that your app supports. When the user selects a restaurant, Apple fills this property with the unique identifier that you provided.

## See Also

### Accessing the Restaurant Information
- [var name: String](./name.md)
  The name of the restaurant.
- [var location: CLLocation](./location.md)
  The location of the restaurant.
- [var vendorIdentifier: String](./vendoridentifier.md)
  The provider of the restaurant data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurant/restaurantidentifier)*