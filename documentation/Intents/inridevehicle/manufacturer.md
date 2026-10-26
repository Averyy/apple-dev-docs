# manufacturer

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the vehicle’s manufacturer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var manufacturer: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * manufacturer;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * manufacturer;
```

#### Discussion

Examples might include “Honda” or “Ford”.

## See Also

### Specifying the Vehicle Description
- [var registrationPlate: String?](./registrationplate.md)
  The text on the license plate or registration plate of the vehicle.
- [var model: String?](./model.md)
  The model of the vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridevehicle/manufacturer)*