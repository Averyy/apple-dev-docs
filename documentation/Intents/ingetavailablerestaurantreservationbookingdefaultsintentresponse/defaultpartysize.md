# defaultPartySize

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The party size to use when placing the initial reservations request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var defaultPartySize: Int { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSUInteger defaultPartySize;
```

*macOS*

```objc
@property (atomic, readonly) NSUInteger defaultPartySize;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

The value you specify in this property represents the likely size of the user’s party. The user can change this value later, but the system uses it when asking your Intents extension to provide an initial set of reservation options. The default party size must fall between the minimum and maximum party sizes supported by the restaurant.

## See Also

### Specifying the Default Values
- [var defaultBookingDate: Date](./defaultbookingdate.md)
  The default booking date to use when placing the initial reservations request.
- [var maximumPartySize: NSNumber?](./maximumpartysize.md)
  The maximum party size allowed by the restaurant.
- [var minimumPartySize: NSNumber?](./minimumpartysize.md)
  The minimum party size allowed by the restaurant.
- [var providerImage: INImage](./providerimage.md)
  An image representing your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse/defaultpartysize)*