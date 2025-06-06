# numberOfCaptureGroups

**Framework**: Foundation  
**Kind**: property

Returns the number of capture groups in the regular expression.

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
var numberOfCaptureGroups: Int { get }
```

#### Discussion

A capture group consists of each possible match within a regular expression. Each capture group can then be used in a replacement template to insert that value into a replacement string.

This value puts a limit on the values of `n` for `$n` in templates, and it determines the number of ranges in the returned [`NSTextCheckingResult`](nstextcheckingresult.md) instances returned in the `match...` methods.

An exception will be generated if you attempt to access a result with an index value exceeding `numberOfCaptureGroups``-1`.

## See Also

- [var pattern: String](nsregularexpression/pattern.md)
  Returns the regular expression pattern.
- [var options: NSRegularExpression.Options](nsregularexpression/options-swift.property.md)
  Returns the options used when the regular expression option was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/numberofcapturegroups)*