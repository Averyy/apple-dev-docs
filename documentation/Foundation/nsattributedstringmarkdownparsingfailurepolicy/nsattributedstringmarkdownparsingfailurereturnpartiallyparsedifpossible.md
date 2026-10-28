# NSAttributedStringMarkdownParsingFailureReturnPartiallyParsedIfPossible

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

A policy to return a partially parsed string, if possible.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```c
NSAttributedStringMarkdownParsingFailureReturnPartiallyParsedIfPossible
```

## Discussion

With this policy, the returned string may include unparsed markup. If returning a partially parsed string isn’t possible, the parser may return an error anyway.

## See Also

### Failure Policies
- [NSAttributedStringMarkdownParsingFailureReturnError](./nsattributedstringmarkdownparsingfailurereturnerror.md)
  A policy to return an error from the initializer if parsing fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringmarkdownparsingfailurepolicy/nsattributedstringmarkdownparsingfailurereturnpartiallyparsedifpossible)*