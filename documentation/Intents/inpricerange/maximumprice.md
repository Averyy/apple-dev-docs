# maximumPrice

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The maximum price.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var maximumPrice: NSDecimalNumber? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) NSDecimalNumber * maximumPrice;
```

*macOS*

```objc
@property (atomic, readonly, nullable) NSDecimalNumber * maximumPrice;
```

#### Discussion

If no maximum price was specified at initialization time, the value in this property is `nil`.

## See Also

### Getting the Price Range Information
- [var minimumPrice: NSDecimalNumber?](./minimumprice.md)
  The minimum price.
- [var currencyCode: String](./currencycode.md)
  The ISO 4217 currency code that applies to the price information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpricerange/maximumprice)*