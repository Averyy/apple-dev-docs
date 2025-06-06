# options

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

The options property specifies aspects of the regular expression matching that are always used when matching the regular expression. For example, if the expression is case sensitive, allows comments, ignores metacharacters, etc. See [`NSRegularExpression.Options`](nsregularexpression/options-swift.struct.md) for a complete discussion of the possible constants and their meanings.

## See Also

- [init(pattern: String, options: NSRegularExpression.Options) throws](nsregularexpression/init(pattern:options:).md)
  Returns an initialized NSRegularExpression instance with the specified regular expression pattern and options.
- [var pattern: String](nsregularexpression/pattern.md)
  Returns the regular expression pattern.
- [var numberOfCaptureGroups: Int](nsregularexpression/numberofcapturegroups.md)
  Returns the number of capture groups in the regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.property)*