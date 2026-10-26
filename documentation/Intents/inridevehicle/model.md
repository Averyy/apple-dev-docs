# model

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The model of the vehicle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var model: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * model;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * model;
```

#### Discussion

Examples might include “Civic” or “Escape”.

## See Also

### Specifying the Vehicle Description
- [var registrationPlate: String?](./registrationplate.md)
  The text on the license plate or registration plate of the vehicle.
- [var manufacturer: String?](./manufacturer.md)
  The name of the vehicle’s manufacturer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridevehicle/model)*