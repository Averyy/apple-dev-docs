# localizedBookingAdvisementText

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A localized, user-readable string containing policies and information related to the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localizedBookingAdvisementText: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * localizedBookingAdvisementText;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * localizedBookingAdvisementText;
```

## Discussion

Use this property to convey restaurant policies, parking instructions, or special information related to the reservation. The system displays this information to the user along with the reservation options. The default value of this property is `nil`.

## See Also

### Specifying Additional Information
- [var localizedRestaurantDescriptionText: String?](./localizedrestaurantdescriptiontext.md)
  A localized, user-readable string containing a description of the restaurant.
- [var termsAndConditions: INTermsAndConditions?](./termsandconditions.md)
  The terms and conditions of using your company’s services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentresponse/localizedbookingadvisementtext)*