# maximumPartySize

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The maximum party size allowed by the restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var maximumPartySize: NSNumber? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSNumber * maximumPartySize;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSNumber * maximumPartySize;
```

## Discussion

Use this property to specify the maximum party size that the restaurant allows. The system provides the user with this information and prevents the user from booking reservations when the party size exceeds this value.

Specify `nil` for this property if there is no maximum party size for the restaurant.

## See Also

### Specifying the Default Values
- [var defaultBookingDate: Date](./defaultbookingdate.md)
  The default booking date to use when placing the initial reservations request.
- [var defaultPartySize: Int](./defaultpartysize.md)
  The party size to use when placing the initial reservations request.
- [var minimumPartySize: NSNumber?](./minimumpartysize.md)
  The minimum party size allowed by the restaurant.
- [var providerImage: INImage](./providerimage.md)
  An image representing your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse/maximumpartysize)*