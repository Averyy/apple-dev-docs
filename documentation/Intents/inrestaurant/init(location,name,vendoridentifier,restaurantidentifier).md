# init(location:name:vendorIdentifier:restaurantIdentifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a restaurant object with some identifying information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(location: CLLocation, name: String, vendorIdentifier: String, restaurantIdentifier: String)
```

```objc
- (instancetype) initWithLocation:(CLLocation *) location name:(NSString *) name vendorIdentifier:(NSString *) vendorIdentifier restaurantIdentifier:(NSString *) restaurantIdentifier;
```

## Return Value

An initialized restaurant object or `nil` if the object could not be created.

## Parameters

- `location`: The location of the restaurant, specified as a geographic map coordinate. This value represents where the restaurant’s marker shows up on the map.
- `name`: The name of the restaurant.
- `vendorIdentifier`: A unique string that identifies the provider of the restaurant data. Typically, this string is your company’s domain name formatted as a reverse-DNS string such as `com.example`.
- `restaurantIdentifier`: The unique identifier that you provided Apple for the specified restaurant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurant/init(location:name:vendoridentifier:restaurantidentifier:))*