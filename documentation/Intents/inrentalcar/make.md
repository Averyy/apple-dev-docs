# make

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the company that made the rental car.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var make: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * make;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * make;
```

## See Also

### Getting the Rental Car Information
- [var rentalCompanyName: String](./rentalcompanyname.md)
  The name of the rental car company.
- [var type: String?](./type.md)
  The type of rental car the user reserved.
- [var model: String?](./model.md)
  The name of the rental car model.
- [var rentalCarDescription: String?](./rentalcardescription.md)
  A description of the rental car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrentalcar/make)*