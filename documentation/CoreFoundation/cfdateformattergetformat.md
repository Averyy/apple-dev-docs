# CFDateFormatterGetFormat(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a format string for the given date formatter object.

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
func CFDateFormatterGetFormat(_ formatter: CFDateFormatter!) -> CFString!
```

#### Return Value

The format string for `formatter` as was specified by calling the [`CFDateFormatterSetFormat(_:_:)`](cfdateformattersetformat(_:_:).md) function, or derived from the date formatter’s date or time styles. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `formatter`: The date formatter to examine.

## See Also

- [func CFDateFormatterCopyProperty(CFDateFormatter!, CFDateFormatterKey!) -> CFTypeRef!](cfdateformattercopyproperty(_:_:).md)
  Returns a copy of a date formatter’s value for a given key.
- [func CFDateFormatterGetDateStyle(CFDateFormatter!) -> CFDateFormatterStyle](cfdateformattergetdatestyle(_:).md)
  Returns the date style used to create the given date formatter object.
- [func CFDateFormatterGetLocale(CFDateFormatter!) -> CFLocale!](cfdateformattergetlocale(_:).md)
  Returns the locale object used to create the given date formatter object.
- [func CFDateFormatterGetTimeStyle(CFDateFormatter!) -> CFDateFormatterStyle](cfdateformattergettimestyle(_:).md)
  Returns the time style used to create the given date formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattergetformat(_:))*