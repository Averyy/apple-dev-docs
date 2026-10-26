# localizedRestaurantDescriptionText

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A localized, user-readable string containing a description of the restaurant.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localizedRestaurantDescriptionText: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * localizedRestaurantDescriptionText;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * localizedRestaurantDescriptionText;
```

#### Discussion

Use this property to provide descriptive information about the restaurant. You are responsible for the contents of this string, Typical descriptions might include a summary of the cuisine offered by the restaurant along with a description of the restaurant’s ambiance, amenities, and services. The default value of this property is `nil`.

## See Also

### Specifying Additional Information
- [var localizedBookingAdvisementText: String?](./localizedbookingadvisementtext.md)
  A localized, user-readable string containing policies and information related to the reservation.
- [var termsAndConditions: INTermsAndConditions?](./termsandconditions.md)
  The terms and conditions of using your company’s services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentresponse/localizedrestaurantdescriptiontext)*