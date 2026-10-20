# roundingBehavior

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The rounding behavior used by the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@NSCopying
var roundingBehavior: NSDecimalNumberHandler { get set }
```

```objc
@property (copy) NSDecimalNumberHandler * roundingBehavior;
```

## See Also

### Configuring Rounding Behavior
- [class NSDecimalNumberHandler](../nsdecimalnumberhandler.md)
  A class that adopts the decimal number behaviors protocol.
- [var roundingIncrement: NSNumber!](./roundingincrement.md)
  The rounding increment used by the receiver.
- [var roundingMode: NumberFormatter.RoundingMode](./roundingmode-swift.property.md)
  The rounding mode used by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/roundingbehavior)*