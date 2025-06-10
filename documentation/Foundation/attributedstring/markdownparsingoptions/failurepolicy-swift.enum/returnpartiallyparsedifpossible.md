# AttributedString.MarkdownParsingOptions.FailurePolicy.returnPartiallyParsedIfPossible

**Framework**: Foundation  
**Kind**: case

A policy to return a partially-parsed string, if possible.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case returnPartiallyParsedIfPossible
```

#### Discussion

With this policy, the returned string may include unparsed markup. If returning a partially parsed string isn’t possible, the parser may throw an error anyway.

## See Also

- [AttributedString.MarkdownParsingOptions.FailurePolicy.throwError](attributedstring/markdownparsingoptions/failurepolicy-swift.enum/throwerror.md)
  A policy to throw an error from the initializer if parsing fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/markdownparsingoptions/failurepolicy-swift.enum/returnpartiallyparsedifpossible)*