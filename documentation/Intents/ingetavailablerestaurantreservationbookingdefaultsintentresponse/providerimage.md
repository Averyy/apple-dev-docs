# providerImage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An image representing your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var providerImage: INImage { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) INImage * providerImage;
```

*macOS*

```objc
@property (atomic, copy) INImage * providerImage;
```

## Discussion

The system displays the image from this property in any interfaces involved in making reservations. For example, the Maps app displays this image as part of the reservations workflow.

## See Also

### Specifying the Default Values
- [var defaultBookingDate: Date](./defaultbookingdate.md)
  The default booking date to use when placing the initial reservations request.
- [var defaultPartySize: Int](./defaultpartysize.md)
  The party size to use when placing the initial reservations request.
- [var maximumPartySize: NSNumber?](./maximumpartysize.md)
  The maximum party size allowed by the restaurant.
- [var minimumPartySize: NSNumber?](./minimumpartysize.md)
  The minimum party size allowed by the restaurant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse/providerimage)*