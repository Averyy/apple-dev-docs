# dropOffLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name and location where the user can drop off the car.

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
var dropOffLocation: CLPlacemark? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) CLPlacemark * dropOffLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) CLPlacemark * dropOffLocation;
```

## See Also

### Getting the Rental Car Reservation Information
- [var rentalCar: INRentalCar](./rentalcar.md)
  An object containing detailed information about the rental car.
- [class INRentalCar](../inrentalcar.md)
  The information that describes a rental car.
- [var rentalDuration: INDateComponentsRange](./rentalduration.md)
  The date and time range that indicates the pickup and drop off times for the rental.
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The name and location where the user can pick up the car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrentalcarreservation/dropofflocation)*