# CFNumberFormatterGetFormat(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a format string for the given number formatter object.

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
func CFNumberFormatterGetFormat(_ formatter: CFNumberFormatter!) -> CFString!
```

#### Return Value

The format string for `formatter` as was specified by calling the [`CFNumberFormatterSetFormat(_:_:)`](cfnumberformattersetformat(_:_:).md) function, or derived from the number formatter’s style. See [`Creating and Using CFNumberFormatter Objects`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/dfCreatingCFNumberFormatters.html#//apple_ref/doc/uid/TP40002342) for more information. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `formatter`: The number formatter to examine.

## See Also

- [func CFNumberFormatterCopyProperty(CFNumberFormatter!, CFNumberFormatterKey!) -> CFTypeRef!](cfnumberformattercopyproperty(_:_:).md)
  Returns a copy of a number formatter’s value for a given key.
- [func CFNumberFormatterGetLocale(CFNumberFormatter!) -> CFLocale!](cfnumberformattergetlocale(_:).md)
  Returns the locale object used to create the given number formatter object.
- [func CFNumberFormatterGetStyle(CFNumberFormatter!) -> CFNumberFormatterStyle](cfnumberformattergetstyle(_:).md)
  Returns the number style used to create the given number formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattergetformat(_:))*