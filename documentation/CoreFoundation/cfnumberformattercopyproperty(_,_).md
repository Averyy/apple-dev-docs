# CFNumberFormatterCopyProperty(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a copy of a number formatter’s value for a given key.

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
func CFNumberFormatterCopyProperty(_ formatter: CFNumberFormatter!, _ key: CFNumberFormatterKey!) -> CFTypeRef!
```

```c
extern CFTypeRefCFNumberFormatterCopyProperty(CFNumberFormatterRef formatter, CFNumberFormatterKey key);
```

#### Return Value

A `CFType` object that is a copy of the property value for `key`. Returns `NULL` if there is no value specified for `key`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `formatter`: The number formatter to examine.
- `key`: A property key. See [Number Formatter Property Keys](./number-formatter-property-keys.md) for valid values.

## See Also

### Examining a Number Formatter
- [func CFNumberFormatterGetFormat(CFNumberFormatter!) -> CFString!](./cfnumberformattergetformat%28_%29.md)
  Returns a format string for the given number formatter object.
- [func CFNumberFormatterGetLocale(CFNumberFormatter!) -> CFLocale!](./cfnumberformattergetlocale%28_%29.md)
  Returns the locale object used to create the given number formatter object.
- [func CFNumberFormatterGetStyle(CFNumberFormatter!) -> CFNumberFormatterStyle](./cfnumberformattergetstyle%28_%29.md)
  Returns the number style used to create the given number formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattercopyproperty(_:_:))*