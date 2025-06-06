# CFDateFormatterGetLocale(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the locale object used to create the given date formatter object.

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
func CFDateFormatterGetLocale(_ formatter: CFDateFormatter!) -> CFLocale!
```

#### Return Value

The locale object used to create `formatter`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `formatter`: The date formatter object to examine.

## See Also

- [func CFDateFormatterCopyProperty(CFDateFormatter!, CFDateFormatterKey!) -> CFTypeRef!](cfdateformattercopyproperty(_:_:).md)
  Returns a copy of a date formatter’s value for a given key.
- [func CFDateFormatterGetDateStyle(CFDateFormatter!) -> CFDateFormatterStyle](cfdateformattergetdatestyle(_:).md)
  Returns the date style used to create the given date formatter object.
- [func CFDateFormatterGetFormat(CFDateFormatter!) -> CFString!](cfdateformattergetformat(_:).md)
  Returns a format string for the given date formatter object.
- [func CFDateFormatterGetTimeStyle(CFDateFormatter!) -> CFDateFormatterStyle](cfdateformattergettimestyle(_:).md)
  Returns the time style used to create the given date formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattergetlocale(_:))*