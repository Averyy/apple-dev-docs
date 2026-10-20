# CFDateFormatterGetTimeStyle(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the time style used to create the given date formatter object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDateFormatterGetTimeStyle(_ formatter: CFDateFormatter!) -> CFDateFormatterStyle
```

```c
extern CFDateFormatterStyle CFDateFormatterGetTimeStyle(CFDateFormatterRef formatter);
```

#### Return Value

The time style used to create `formatter`.

## Parameters

- `formatter`: The date formatter to examine.

## See Also

### Getting Information About a Date Formatter
- [func CFDateFormatterCopyProperty(CFDateFormatter!, CFDateFormatterKey!) -> CFTypeRef!](./cfdateformattercopyproperty%28_,_%29.md)
  Returns a copy of a date formatter’s value for a given key.
- [func CFDateFormatterGetDateStyle(CFDateFormatter!) -> CFDateFormatterStyle](./cfdateformattergetdatestyle%28_%29.md)
  Returns the date style used to create the given date formatter object.
- [func CFDateFormatterGetFormat(CFDateFormatter!) -> CFString!](./cfdateformattergetformat%28_%29.md)
  Returns a format string for the given date formatter object.
- [func CFDateFormatterGetLocale(CFDateFormatter!) -> CFLocale!](./cfdateformattergetlocale%28_%29.md)
  Returns the locale object used to create the given date formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattergettimestyle(_:))*