# model

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The manufacturer’s model name for the electric vehicle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var model: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * model;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * model;
```

## Discussion

Maps displays this value when it presents information about the electric vehicle.

## See Also

### Getting the Car’s Attributes
- [var make: String?](./make.md)
  The electric vehicle’s manufacturer.
- [var color: CGColor?](./color.md)
  The electric vehicle’s color.
- [var year: String?](./year.md)
  The electric vehicle’s year of manufacture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/model)*