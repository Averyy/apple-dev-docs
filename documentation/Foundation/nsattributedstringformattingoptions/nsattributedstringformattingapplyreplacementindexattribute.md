# NSAttributedStringFormattingApplyReplacementIndexAttribute

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

An option to apply to the replaced portions of text in a format string.

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
NSAttributedStringFormattingApplyReplacementIndexAttribute
```

#### Discussion

When creating an attributed string from a format string, specify this option to apply an attribute to all substituted text. Consider the creation of an attributed string using the format string `“Count: %d; Total: %d”`. After generating the attributed string, the creation method applies the [`replacementIndex`](../nsattributedstring/key/replacementindex.md) attribute to the both integer values in the resulting string.

The value of the [`replacementIndex`](../nsattributedstring/key/replacementindex.md) attribute is an `NSNumber` with the replacement’s position in the format string. The value for the first replacement is 1, for the second replacement is 2, and so on. If you include a positional marker in the format string specifier, the value of the attribute reflects that position, regardless of its actual position in the string. For example, the string `“%2@ -- %1@”` causes the first argument to have an index value of `2` and the second argument to have an index value of `1`.

## See Also

### Getting the formatting options
- [NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging](./nsattributedstringformattinginsertargumentattributeswithoutmerging.md)
  An option to replace the attributes in a substituted string with those of the provided attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringformattingoptions/nsattributedstringformattingapplyreplacementindexattribute)*