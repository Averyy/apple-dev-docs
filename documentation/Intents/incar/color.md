# color

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The electric vehicle’s color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var color: CGColor? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) CGColorRef color;
```

*macOS*

```objc
@property (atomic, readonly, nullable) CGColorRef color;
```

## Discussion

Maps displays this value when it presents information about the electric vehicle.

## See Also

### Getting the Car’s Attributes
- [var make: String?](./make.md)
  The electric vehicle’s manufacturer.
- [var model: String?](./model.md)
  The manufacturer’s model name for the electric vehicle.
- [var year: String?](./year.md)
  The electric vehicle’s year of manufacture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/color)*