# year

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The electric vehicle’s year of manufacture.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var year: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * year;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * year;
```

## Discussion

Maps displays this value when it presents information about the electric vehicle.

## See Also

### Getting the Car’s Attributes
- [var make: String?](./make.md)
  The electric vehicle’s manufacturer.
- [var model: String?](./model.md)
  The manufacturer’s model name for the electric vehicle.
- [var color: CGColor?](./color.md)
  The electric vehicle’s color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/year)*