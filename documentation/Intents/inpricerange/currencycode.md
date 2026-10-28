# currencyCode

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The ISO 4217 currency code that applies to the price information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var currencyCode: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSString * currencyCode;
```

*macOS*

```objc
@property (atomic, readonly) NSString * currencyCode;
```

## Discussion

To retrieve the list of available currency codes, call the [`isoCurrencyCodes`](../../Foundation/nslocale/isocurrencycodes.md) method of the [`NSLocale`](../../Foundation/nslocale.md) class.

## See Also

### Getting the Price Range Information
- [var minimumPrice: NSDecimalNumber?](./minimumprice.md)
  The minimum price.
- [var maximumPrice: NSDecimalNumber?](./maximumprice.md)
  The maximum price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpricerange/currencycode)*