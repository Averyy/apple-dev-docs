# location

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location of the restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var location: CLLocation { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) CLLocation * location;
```

*macOS*

```objc
@property (atomic, copy) CLLocation * location;
```

## Discussion

This value represents the location on the map where the restaurant’s marker appears.

## See Also

### Accessing the Restaurant Information
- [var name: String](./name.md)
  The name of the restaurant.
- [var restaurantIdentifier: String](./restaurantidentifier.md)
  A unique identifier for the restaurant.
- [var vendorIdentifier: String](./vendoridentifier.md)
  The provider of the restaurant data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurant/location)*