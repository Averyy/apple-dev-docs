# reservationItemReferences

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of unique identifiers for previously created reservations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var reservationItemReferences: [INSpeakableString]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INSpeakableString *> * reservationItemReferences;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INSpeakableString *> * reservationItemReferences;
```

## Discussion

This property contains an array of unique identifiers for user-created reservations. You can provide a textual representation for this property, such as “Flight to Los Angeles” to describe an airline reservation.

## See Also

### Accessing a Reservation
- [var reservationContainerReference: INSpeakableString?](./reservationcontainerreference.md)
  A unique identifier for the array containing the reservation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintent/reservationitemreferences)*