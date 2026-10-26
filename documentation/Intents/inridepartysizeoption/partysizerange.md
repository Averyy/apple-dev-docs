# partySizeRange

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The number of people in the party, specified as a minimum and maximum value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var partySizeRange: NSRange { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSRange partySizeRange;
```

*macOS*

```objc
@property (atomic, readonly) NSRange partySizeRange;
```

#### Discussion

The `location` value of the range contains the minimum number of people. Adding the `location` and `length` values results in the maximum number of people. For example, a range value of (1, 0) represents a single person and a range value of (1, 2) represents 1 to 3 people.

## See Also

### Getting the Party Size Information
- [var sizeDescription: String](./sizedescription.md)
  The user-visible description of the party size.
- [var priceRange: INPriceRange?](./pricerange.md)
  The pricing information for parties of the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridepartysizeoption/partysizerange)*