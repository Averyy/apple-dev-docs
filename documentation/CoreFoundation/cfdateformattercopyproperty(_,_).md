# CFDateFormatterCopyProperty(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a copy of a date formatter’s value for a given key.

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
func CFDateFormatterCopyProperty(_ formatter: CFDateFormatter!, _ key: CFDateFormatterKey!) -> CFTypeRef!
```

```c
extern CFTypeRefCFDateFormatterCopyProperty(CFDateFormatterRef formatter, CFDateFormatterKey key);
```

#### Return Value

A CFType object that is a copy of the property value for `key`, or `NULL` if there is no value specified for `key`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `formatter`: The date formatter to examine.
- `key`: The property key for the value to obtain. See [Date Formatter Property Keys](./date-formatter-property-keys.md) for a description of possible values for this parameter.

## See Also

### Getting Information About a Date Formatter
- [func CFDateFormatterGetDateStyle(CFDateFormatter!) -> CFDateFormatterStyle](./cfdateformattergetdatestyle%28_%29.md)
  Returns the date style used to create the given date formatter object.
- [func CFDateFormatterGetFormat(CFDateFormatter!) -> CFString!](./cfdateformattergetformat%28_%29.md)
  Returns a format string for the given date formatter object.
- [func CFDateFormatterGetLocale(CFDateFormatter!) -> CFLocale!](./cfdateformattergetlocale%28_%29.md)
  Returns the locale object used to create the given date formatter object.
- [func CFDateFormatterGetTimeStyle(CFDateFormatter!) -> CFDateFormatterStyle](./cfdateformattergettimestyle%28_%29.md)
  Returns the time style used to create the given date formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattercopyproperty(_:_:))*