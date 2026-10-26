# make

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The electric vehicle’s manufacturer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

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

#### Discussion

Maps displays this value when it presents information about the electric vehicle.

## See Also

### Getting the Car’s Attributes
- [var model: String?](./model.md)
  The manufacturer’s model name for the electric vehicle.
- [var color: CGColor?](./color.md)
  The electric vehicle’s color.
- [var year: String?](./year.md)
  The electric vehicle’s year of manufacture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incar/make)*