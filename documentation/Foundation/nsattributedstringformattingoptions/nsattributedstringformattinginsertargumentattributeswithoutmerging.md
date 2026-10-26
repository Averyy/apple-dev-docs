# NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

An option to replace the attributes in a substituted string with those of the provided attributed string.

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
NSAttributedStringFormattingInsertArgumentAttributesWithoutMerging
```

#### Discussion

This option applies when a format string includes the %@ format string specifier and the substituted value is an attributed string. If you include this option, the creation method prefers the attributes in the substitute attributed string over the attributes in the format string. If you don’t include this option, the creation method prefers the attributes from the format string over those in the substitute string.

Consider a format string `“Name: %@”` that applies a red text color to the substituted value, and consider an attributed string that applies green text using the same attribute. If you don’t include this option, the substituted text in the new string is red. If you include the option, the substituted text is green. This option affects only attributes that are common to both the format string and the substitute string.

If a creation method doesn’t let you specify options, it behaves as if this option isn’t present.

## See Also

### Getting the formatting options
- [NSAttributedStringFormattingApplyReplacementIndexAttribute](./nsattributedstringformattingapplyreplacementindexattribute.md)
  An option to apply to the replaced portions of text in a format string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstringformattingoptions/nsattributedstringformattinginsertargumentattributeswithoutmerging)*