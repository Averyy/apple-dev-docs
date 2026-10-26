# reservations

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array containing reservations reqeusted by the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var reservations: [INReservation]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INReservation *> * reservations;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INReservation *> * reservations;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintentresponse/reservations)*