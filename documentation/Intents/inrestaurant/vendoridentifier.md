# vendorIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The provider of the restaurant data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var vendorIdentifier: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * vendorIdentifier;
```

*macOS*

```objc
@property (atomic, copy) NSString * vendorIdentifier;
```

## Discussion

Each provider of restaurant data has a unique identifier assigned to it by Apple. Typically, this string is your company’s domain name formatted as a reverse-DNS string such as `com.example`. You can use this string to verify that the restaurant information belongs to your company.

## See Also

### Accessing the Restaurant Information
- [var name: String](./name.md)
  The name of the restaurant.
- [var location: CLLocation](./location.md)
  The location of the restaurant.
- [var restaurantIdentifier: String](./restaurantidentifier.md)
  A unique identifier for the restaurant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurant/vendoridentifier)*