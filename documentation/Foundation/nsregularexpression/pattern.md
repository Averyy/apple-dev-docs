# pattern

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the regular expression pattern.

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
var pattern: String { get }
```

```objc
@property (copy, readonly) NSString * pattern;
```

## See Also

### Related Documentation
- [init(pattern: String, options: NSRegularExpression.Options) throws](./init%28pattern,options%29.md)
  Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.
- [+ regularExpressionWithPattern:options:error:](./regularexpressionwithpattern_options_error_.md)
  Creates an NSRegularExpression instance with the specified regular expression pattern and options.
### Getting the Regular Expression and Options
- [var options: NSRegularExpression.Options](./options-swift.property.md)
  Returns the options used when the regular expression option was created.
- [var numberOfCaptureGroups: Int](./numberofcapturegroups.md)
  Returns the number of capture groups in the regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/pattern)*