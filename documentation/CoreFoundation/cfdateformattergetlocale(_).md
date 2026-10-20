# CFDateFormatterGetLocale(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the locale object used to create the given date formatter object.

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
func CFDateFormatterGetLocale(_ formatter: CFDateFormatter!) -> CFLocale!
```

```c
extern CFLocaleRefCFDateFormatterGetLocale(CFDateFormatterRef formatter);
```

#### Return Value

The locale object used to create `formatter`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `formatter`: The date formatter object to examine.

## See Also

### Getting Information About a Date Formatter
- [func CFDateFormatterCopyProperty(CFDateFormatter!, CFDateFormatterKey!) -> CFTypeRef!](./cfdateformattercopyproperty%28_,_%29.md)
  Returns a copy of a date formatter’s value for a given key.
- [func CFDateFormatterGetDateStyle(CFDateFormatter!) -> CFDateFormatterStyle](./cfdateformattergetdatestyle%28_%29.md)
  Returns the date style used to create the given date formatter object.
- [func CFDateFormatterGetFormat(CFDateFormatter!) -> CFString!](./cfdateformattergetformat%28_%29.md)
  Returns a format string for the given date formatter object.
- [func CFDateFormatterGetTimeStyle(CFDateFormatter!) -> CFDateFormatterStyle](./cfdateformattergettimestyle%28_%29.md)
  Returns the time style used to create the given date formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattergetlocale(_:))*