# format

**Framework**: Foundation  
**Kind**: property

The receiver’s format.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var format: String { get set }
```

#### Discussion

The format string uses the format patterns from [`Unicode Technical Standard #35`](https://developer.apple.comhttp://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns).  For more information, see  [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

## See Also

- [var formattingContext: Formatter.Context](numberformatter/formattingcontext.md)
  The capitalization formatting context used when formatting a number.
- [var formatWidth: Int](numberformatter/formatwidth.md)
  The format width used by the receiver.
- [var negativeFormat: String!](numberformatter/negativeformat.md)
  The format the receiver uses to display negative values.
- [var positiveFormat: String!](numberformatter/positiveformat.md)
  The format the receiver uses to display positive values.
- [var multiplier: NSNumber?](numberformatter/multiplier.md)
  The multiplier of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/format)*