# multiplier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The multiplier of the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var multiplier: NSNumber? { get set }
```

```objc
@property (copy, nullable) NSNumber * multiplier;
```

#### Discussion

A multiplier is a factor used in conversions between numbers and strings (that is, numbers as stored and numbers as displayed). When the input value is a string, the multiplier is used to divide, and when the input value is a number, the multiplier is used to multiply. These operations allow the formatted values to be different from the values that a program manipulates internally.

## See Also

### Configuring Numeric Formats
- [var format: String](./format.md)
  The receiver’s format.
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  The capitalization formatting context used when formatting a number.
- [var formatWidth: Int](./formatwidth.md)
  The format width used by the receiver.
- [var negativeFormat: String!](./negativeformat.md)
  The format the receiver uses to display negative values.
- [var positiveFormat: String!](./positiveformat.md)
  The format the receiver uses to display positive values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/multiplier)*