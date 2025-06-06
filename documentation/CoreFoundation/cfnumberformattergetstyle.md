# CFNumberFormatterGetStyle(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number style used to create the given number formatter object.

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
func CFNumberFormatterGetStyle(_ formatter: CFNumberFormatter!) -> CFNumberFormatterStyle
```

#### Return Value

The number style used to create `formatter`.

## Parameters

- `formatter`: The number formatter to examine.

## See Also

- [func CFNumberFormatterCopyProperty(CFNumberFormatter!, CFNumberFormatterKey!) -> CFTypeRef!](cfnumberformattercopyproperty(_:_:).md)
  Returns a copy of a number formatter’s value for a given key.
- [func CFNumberFormatterGetFormat(CFNumberFormatter!) -> CFString!](cfnumberformattergetformat(_:).md)
  Returns a format string for the given number formatter object.
- [func CFNumberFormatterGetLocale(CFNumberFormatter!) -> CFLocale!](cfnumberformattergetlocale(_:).md)
  Returns the locale object used to create the given number formatter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattergetstyle(_:))*