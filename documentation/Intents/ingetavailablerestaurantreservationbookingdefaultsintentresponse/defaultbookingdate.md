# defaultBookingDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The default booking date to use when placing the initial reservations request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var defaultBookingDate: Date { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSDate * defaultBookingDate;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSDate * defaultBookingDate;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

The value you specify in this property should be the date and time you think the user is most likely to choose. The user can change this date later, but the system uses it when asking your Intents extension to provide an initial set of reservation options. The date should take into account the hours in which the restaurant is open and should also reflect a date when making a reservation is possible. Do not specify a date on which the restaurant is closed or fully booked.

## See Also

### Specifying the Default Values
- [var defaultPartySize: Int](./defaultpartysize.md)
  The party size to use when placing the initial reservations request.
- [var maximumPartySize: NSNumber?](./maximumpartysize.md)
  The maximum party size allowed by the restaurant.
- [var minimumPartySize: NSNumber?](./minimumpartysize.md)
  The minimum party size allowed by the restaurant.
- [var providerImage: INImage](./providerimage.md)
  An image representing your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse/defaultbookingdate)*