# sizeDescription

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user-visible description of the party size.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var sizeDescription: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSString * sizeDescription;
```

*macOS*

```objc
@property (atomic, readonly) NSString * sizeDescription;
```

#### Discussion

When presenting party size options to the user, SiriKit displays this string.

## See Also

### Getting the Party Size Information
- [var partySizeRange: NSRange](./partysizerange.md)
  The number of people in the party, specified as a minimum and maximum value.
- [var priceRange: INPriceRange?](./pricerange.md)
  The pricing information for parties of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridepartysizeoption/sizedescription)*