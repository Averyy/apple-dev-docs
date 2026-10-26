# options

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the options used when the regular expression option was created.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var options: NSRegularExpression.Options { get }
```

```objc
@property (readonly) NSRegularExpressionOptions options;
```

#### Discussion

The options property specifies aspects of the regular expression matching that are always used when matching the regular expression. For example, if the expression is case sensitive, allows comments, ignores metacharacters, etc. See [`NSRegularExpression.Options`](./options-swift.struct.md) for a complete discussion of the possible constants and their meanings.

## See Also

### Related Documentation
- [init(pattern: String, options: NSRegularExpression.Options) throws](./init%28pattern,options%29.md)
  Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.
- [+ regularExpressionWithPattern:options:error:](./regularexpressionwithpattern_options_error_.md)
  Creates an NSRegularExpression instance with the specified regular expression pattern and options.
### Getting the Regular Expression and Options
- [var pattern: String](./pattern.md)
  Returns the regular expression pattern.
- [var numberOfCaptureGroups: Int](./numberofcapturegroups.md)
  Returns the number of capture groups in the regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.property)*