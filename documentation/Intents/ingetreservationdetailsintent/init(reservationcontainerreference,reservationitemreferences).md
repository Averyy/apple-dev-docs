# init(reservationContainerReference:reservationItemReferences:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an intent that describes the reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(reservationContainerReference: INSpeakableString?, reservationItemReferences: [INSpeakableString]?)
```

```objc
- (instancetype) initWithReservationContainerReference:(INSpeakableString *) reservationContainerReference reservationItemReferences:(NSArray<INSpeakableString *> *) reservationItemReferences;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

The [`INGetReservationDetailsIntent`](../ingetreservationdetailsintent.md) object should include information about the reservation that accurately represents the content, where to find it, and where to add it.

## Parameters

- `reservationContainerReference`: An [`INSpeakableString`](../inspeakablestring.md) that uniquely identifies the [`reservationItemReferences`](./reservationitemreferences.md) array.
- `reservationItemReferences`: An array of [`INSpeakableString`](../inspeakablestring.md) objects in which each object uniquely identifies a single reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintent/init(reservationcontainerreference:reservationitemreferences:))*