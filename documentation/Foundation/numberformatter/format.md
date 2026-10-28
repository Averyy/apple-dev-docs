# format

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s format.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var format: String { get set }
```

```objc
@property (copy) NSString * format;
```

## Discussion

The format string uses the format patterns from [Unicode Technical Standard #35](http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns).  For more information, see  [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

## See Also

### Configuring Numeric Formats
- [var formattingContext: Formatter.Context](./formattingcontext.md)
  The capitalization formatting context used when formatting a number.
- [var formatWidth: Int](./formatwidth.md)
  The format width used by the receiver.
- [var negativeFormat: String!](./negativeformat.md)
  The format the receiver uses to display negative values.
- [var positiveFormat: String!](./positiveformat.md)
  The format the receiver uses to display positive values.
- [var multiplier: NSNumber?](./multiplier.md)
  The multiplier of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatter/format)*