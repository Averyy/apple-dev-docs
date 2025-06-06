# formattingContext

**Framework**: Foundation  
**Kind**: property

The capitalization formatting context used when formatting a number.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var formattingContext: Formatter.Context { get set }
```

#### Discussion

Defaults to NSFormattingContextUnknown.

## See Also

- [var format: String](numberformatter/format.md)
  The receiver’s format.
- [var formatWidth: Int](numberformatter/formatwidth.md)
  The format width used by the receiver.
- [var negativeFormat: String!](numberformatter/negativeformat.md)
  The format the receiver uses to display negative values.
- [var positiveFormat: String!](numberformatter/positiveformat.md)
  The format the receiver uses to display positive values.
- [var multiplier: NSNumber?](numberformatter/multiplier.md)
  The multiplier of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/formattingcontext)*