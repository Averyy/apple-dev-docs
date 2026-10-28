# initWithDateFormat:allowNaturalLanguage:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes and returns an `NSDateFormatter` instance that uses the OS X 10.0 formatting behavior and the given date format string in its conversions.

**Availability**:
- macOS 10.4+ - Deprecated in 10.9

## Declaration

```objc
- (id) initWithDateFormat:(NSString *) format allowNaturalLanguage:(BOOL) flag;
```

## Return Value

An initialized `NSDateFormatter` instance that uses `format` in its conversions and that *uses the OS X 10.0 formatting behavior*.

## Discussion

`NSDateFormatter` attempts natural-language processing only after it fails to interpret an entered string according to `format`. Natural-language processing supports only a limited set of colloquial phrases, primarily in English. It may give unexpected results, and its use is strongly discouraged.

The following example creates a date formatter with the format string (for example) “Mar 15 1994” and then associates the formatter with the cells of a form (`contactsForm`):

```objc
NSDateFormatter *dateFormat = [[NSDateFormatter alloc]
    initWithDateFormat:@"%b %d %Y" allowNaturalLanguage:NO];
[[contactsForm cells] makeObjectsPerformSelector:@selector(setFormatter:)
     withObject:dateFormat];
```

### Special Considerations

You cannot use this method to initialize a formatter with the OS X 10.4 formatting behavior, you must use `init`.

## Parameters

- `format`: The format for the receiver. See [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i) for a list of conversion specifiers permitted in date format strings.
- `flag`: A flag that specifies whether the receiver should process dates entered as expressions in the vernacular (for example, “tomorrow”)—[`true`](../../Swift/true.md) means that it should.

## See Also

### Related Documentation
- [var doesRelativeDateFormatting: Bool](../dateformatter/doesrelativedateformatting.md)
  A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.
- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
### Deprecated
- [var generatesCalendarDates: Bool](../dateformatter/generatescalendardates.md)
  Indicates whether the formatter generates the deprecated calendar date type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateformatter/initwithdateformat:allownaturallanguage:)*