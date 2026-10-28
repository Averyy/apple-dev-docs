# registrationPlate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The text on the license plate or registration plate of the vehicle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var registrationPlate: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * registrationPlate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * registrationPlate;
```

## Discussion

Examples might include “1JBO007” or “SL68 APL” depending on the format used in the specific country or region where the driver registered the car.

## See Also

### Specifying the Vehicle Description
- [var manufacturer: String?](./manufacturer.md)
  The name of the vehicle’s manufacturer.
- [var model: String?](./model.md)
  The model of the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridevehicle/registrationplate)*