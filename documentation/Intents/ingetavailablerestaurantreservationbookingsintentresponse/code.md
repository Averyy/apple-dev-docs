# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var code: INGetAvailableRestaurantReservationBookingsIntentCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INGetAvailableRestaurantReservationBookingsIntentCode code;
```

*macOS*

```objc
@property (atomic, readonly) INGetAvailableRestaurantReservationBookingsIntentCode code;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INGetAvailableRestaurantReservationBookingsIntentCode](../ingetavailablerestaurantreservationbookingsintentcode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintentresponse/code)*