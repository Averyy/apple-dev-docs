# formatWidth

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The format width used by the receiver.

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
var formatWidth: Int { get set }
```

```objc
@property NSUInteger formatWidth;
```

#### Discussion

The format width is the number of characters of a formatted number within a string that is either left justified or right justified based on the value contained in  [`paddingPosition`](./paddingposition.md).

## See Also

### Configuring Numeric Formats
- [var format: String](./format.md)
  The receiver’s format.
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  The capitalization formatting context used when formatting a number.
- [var negativeFormat: String!](./negativeformat.md)
  The format the receiver uses to display negative values.
- [var positiveFormat: String!](./positiveformat.md)
  The format the receiver uses to display positive values.
- [var multiplier: NSNumber?](./multiplier.md)
  The multiplier of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/formatwidth)*