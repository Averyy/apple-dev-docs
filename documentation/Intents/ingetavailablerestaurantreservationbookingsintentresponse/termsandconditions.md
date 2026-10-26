# termsAndConditions

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The terms and conditions of using your company’s services.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var termsAndConditions: INTermsAndConditions? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INTermsAndConditions * termsAndConditions;
```

*macOS*

```objc
@property (atomic, copy, nullable) INTermsAndConditions * termsAndConditions;
```

#### Discussion

Use this property to specify any terms and conditions that apply to using your booking service. The default value of this property is `nil`.

## See Also

### Specifying Additional Information
- [var localizedRestaurantDescriptionText: String?](./localizedrestaurantdescriptiontext.md)
  A localized, user-readable string containing a description of the restaurant.
- [var localizedBookingAdvisementText: String?](./localizedbookingadvisementtext.md)
  A localized, user-readable string containing policies and information related to the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentresponse/termsandconditions)*