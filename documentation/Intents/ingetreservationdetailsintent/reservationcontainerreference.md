# reservationContainerReference

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the array containing the reservation objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var reservationContainerReference: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * reservationContainerReference;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * reservationContainerReference;
```

## Discussion

This property contains an [`INSpeakableString`](../inspeakablestring.md) that serves as an identifier for the list of reservations about which the user requested details. Set the [`vocabularyIdentifier`](../inspeakable/vocabularyidentifier.md) property to a string that uniquely identifies the group of reservations within your app and the [`spokenPhrase`](../inspeakable/spokenphrase.md) property to a string that makes sense to the user when displayed.

## See Also

### Accessing a Reservation
- [var reservationItemReferences: [INSpeakableString]?](./reservationitemreferences.md)
  An array of unique identifiers for previously created reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintent/reservationcontainerreference)*