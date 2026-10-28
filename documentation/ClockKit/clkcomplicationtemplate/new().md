# new()

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Creating a template without parameters is deprecated in watchOS 7.0. Use a factory method with parameters instead.

## Declaration

```swift
class func new() -> Self
```

```objc
+ (instancetype) new;
```

## Discussion

You shouldn’t create instances of this class directly. Instead, you create instances of one of the concrete subclasses and use the resulting object to specify the data for your complication.

## See Also

### Creating Empty Templates
- [init()](./init%28%29.md)
  Creates a new complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate/new())*