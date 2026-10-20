# init()

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new complication.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Initializing a template without parameters is deprecated in watchOS 7.0. Use an init with parameters instead.

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Discussion

You shouldn’t create instances of this class directly. Instead, you create instances of one of the concrete subclasses and use the resulting object to specify the data for your complication.

## See Also

### Creating Empty Templates
- [class func new() -> Self](./new%28%29.md)
  Returns a new complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate/init())*