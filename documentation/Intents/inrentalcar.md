# INRentalCar

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a rental car.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INRentalCar
```

```objc
@interface INRentalCar : NSObject
```

## Topics

### Creating a Rental Car Object
- [init(rentalCompanyName: String, type: String?, make: String?, model: String?, rentalCarDescription: String?)](./inrentalcar/init%28rentalcompanyname,type,make,model,rentalcardescription%29.md)
  Creates a new rental car object with the specified contents and attributes.
### Getting the Rental Car Information
- [var rentalCompanyName: String](./inrentalcar/rentalcompanyname.md)
  The name of the rental car company.
- [var type: String?](./inrentalcar/type.md)
  The type of rental car the user reserved.
- [var make: String?](./inrentalcar/make.md)
  The name of the company that made the rental car.
- [var model: String?](./inrentalcar/model.md)
  The name of the rental car model.
- [var rentalCarDescription: String?](./inrentalcar/rentalcardescription.md)
  A description of the rental car.
### Initializers
- [init?(coder: NSCoder)](./inrentalcar/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Getting the Rental Car Reservation Information
- [var rentalCar: INRentalCar](./inrentalcarreservation/rentalcar.md)
  An object containing detailed information about the rental car.
- [var rentalDuration: INDateComponentsRange](./inrentalcarreservation/rentalduration.md)
  The date and time range that indicates the pickup and drop off times for the rental.
- [var pickupLocation: CLPlacemark?](./inrentalcarreservation/pickuplocation.md)
  The name and location where the user can pick up the car.
- [var dropOffLocation: CLPlacemark?](./inrentalcarreservation/dropofflocation.md)
  The name and location where the user can drop off the car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrentalcar)*