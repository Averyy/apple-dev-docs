# rentalCarDescription

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A description of the rental car.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var rentalCarDescription: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * rentalCarDescription;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * rentalCarDescription;
```

#### Discussion

This property contains a string that describes the rental car, such as “4 door sedan with air conditioning and an automatic transmission”.

## See Also

### Getting the Rental Car Information
- [var rentalCompanyName: String](./rentalcompanyname.md)
  The name of the rental car company.
- [var type: String?](./type.md)
  The type of rental car the user reserved.
- [var make: String?](./make.md)
  The name of the company that made the rental car.
- [var model: String?](./model.md)
  The name of the rental car model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrentalcar/rentalcardescription)*