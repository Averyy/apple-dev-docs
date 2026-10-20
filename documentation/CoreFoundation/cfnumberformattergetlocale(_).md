# CFNumberFormatterGetLocale(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the locale object used to create the given number formatter object.

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
func CFNumberFormatterGetLocale(_ formatter: CFNumberFormatter!) -> CFLocale!
```

```c
extern CFLocaleRefCFNumberFormatterGetLocale(CFNumberFormatterRef formatter);
```

#### Return Value

The locale used to create `formatter`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `formatter`: The number formatter to examine.

## See Also

### Examining a Number Formatter
- [func CFNumberFormatterCopyProperty(CFNumberFormatter!, CFNumberFormatterKey!) -> CFTypeRef!](./cfnumberformattercopyproperty%28_,_%29.md)
  Returns a copy of a number formatter’s value for a given key.
- [func CFNumberFormatterGetFormat(CFNumberFormatter!) -> CFString!](./cfnumberformattergetformat%28_%29.md)
  Returns a format string for the given number formatter object.
- [func CFNumberFormatterGetStyle(CFNumberFormatter!) -> CFNumberFormatterStyle](./cfnumberformattergetstyle%28_%29.md)
  Returns the number style used to create the given number formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattergetlocale(_:))*