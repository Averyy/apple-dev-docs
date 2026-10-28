# allowsNaturalLanguage

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver attempts to process dates entered as a vernacular string.

**Availability**:
- macOS 10.4+ - Deprecated in 10.9

## Declaration

```objc
- (BOOL) allowsNaturalLanguage;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver attempts to process dates entered as a vernacular string (“today,” “next week,” “dinner time,” and so on), otherwise [`false`](../../Swift/false.md).

## Discussion

Natural-language processing supports only a limited set of colloquial phrases, primarily in English. It may give unexpected results, and its use is strongly discouraged.

### Special Considerations

This method is for use with formatters using `NSDateFormatterBehavior10_0` behavior.

## See Also

### Managing Natural Language Support
- [var isLenient: Bool](../dateformatter/islenient.md)
  A Boolean value that indicates whether the receiver uses heuristics when parsing a string.
- [var doesRelativeDateFormatting: Bool](../dateformatter/doesrelativedateformatting.md)
  A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateformatter/allowsnaturallanguage)*