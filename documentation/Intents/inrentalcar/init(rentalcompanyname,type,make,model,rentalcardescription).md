# init(rentalCompanyName:type:make:model:rentalCarDescription:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new rental car object with the specified contents and attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(rentalCompanyName: String, type: String?, make: String?, model: String?, rentalCarDescription: String?)
```

```objc
- (instancetype) initWithRentalCompanyName:(NSString *) rentalCompanyName type:(NSString *) type make:(NSString *) make model:(NSString *) model rentalCarDescription:(NSString *) rentalCarDescription;
```

## Return Value

A new [`INRentalCar`](../inrentalcar.md) object or `nil` if one can’t be created.

## Parameters

- `rentalCompanyName`: The name of the rental car company.
- `type`: The type of rental car. For example, “Economy Class”.
- `make`: The name of the rental car maker.
- `model`: The name of the rental car model.
- `rentalCarDescription`: A description of the rental car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrentalcar/init(rentalcompanyname:type:make:model:rentalcardescription:))*