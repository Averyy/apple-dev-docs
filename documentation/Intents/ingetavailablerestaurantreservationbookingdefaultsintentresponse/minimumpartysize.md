# minimumPartySize

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The minimum party size allowed by the restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var minimumPartySize: NSNumber? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSNumber * minimumPartySize;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSNumber * minimumPartySize;
```

## Discussion

Use this property to specify the minimum party size that the restaurant allows. The system provides the user with this information and prevents the user from booking reservations when the party size is below this value.

Specify `nil` for this property if there is no minimum party size for the restaurant.

## See Also

### Specifying the Default Values
- [var defaultBookingDate: Date](./defaultbookingdate.md)
  The default booking date to use when placing the initial reservations request.
- [var defaultPartySize: Int](./defaultpartysize.md)
  The party size to use when placing the initial reservations request.
- [var maximumPartySize: NSNumber?](./maximumpartysize.md)
  The maximum party size allowed by the restaurant.
- [var providerImage: INImage](./providerimage.md)
  An image representing your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse/minimumpartysize)*