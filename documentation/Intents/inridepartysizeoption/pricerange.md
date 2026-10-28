# priceRange

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The pricing information for parties of the specified size.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var priceRange: INPriceRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) INPriceRange * priceRange;
```

*macOS*

```objc
@property (atomic, readonly, nullable) INPriceRange * priceRange;
```

## Discussion

When presenting pricing information for this party size, SiriKit displays a formatted version of this value.

## See Also

### Getting the Party Size Information
- [var partySizeRange: NSRange](./partysizerange.md)
  The number of people in the party, specified as a minimum and maximum value.
- [var sizeDescription: String](./sizedescription.md)
  The user-visible description of the party size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridepartysizeoption/pricerange)*