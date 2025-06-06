# CFDateFormatterGetDateStyle(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the date style used to create the given date formatter object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFDateFormatterGetDateStyle(_ formatter: CFDateFormatter!) -> CFDateFormatterStyle
```

#### Return Value

The date style used to create `formatter`.

## Parameters

- `formatter`: The date formatter to examine.

## See Also

- [func CFDateFormatterCopyProperty(CFDateFormatter!, CFDateFormatterKey!) -> CFTypeRef!](cfdateformattercopyproperty(_:_:).md)
  Returns a copy of a date formatter’s value for a given key.
- [func CFDateFormatterGetFormat(CFDateFormatter!) -> CFString!](cfdateformattergetformat(_:).md)
  Returns a format string for the given date formatter object.
- [func CFDateFormatterGetLocale(CFDateFormatter!) -> CFLocale!](cfdateformattergetlocale(_:).md)
  Returns the locale object used to create the given date formatter object.
- [func CFDateFormatterGetTimeStyle(CFDateFormatter!) -> CFDateFormatterStyle](cfdateformattergettimestyle(_:).md)
  Returns the time style used to create the given date formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattergetdatestyle(_:))*