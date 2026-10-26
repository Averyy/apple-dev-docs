# advisementText

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A user-readable string containing policies and information related to the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var advisementText: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * advisementText;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * advisementText;
```

#### Discussion

Use this property to store restaurant policies, parking instructions, or special information related to the reservation. The system displays the information in this string to the user along with the reservation details.

## See Also

### Accessing Special Offers
- [var selectedOffer: INRestaurantOffer?](./selectedoffer.md)
  The offer selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking/advisementtext)*