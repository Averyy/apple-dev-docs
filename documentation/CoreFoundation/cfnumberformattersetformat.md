# CFNumberFormatterSetFormat(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the format string of a number formatter.

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
func CFNumberFormatterSetFormat(_ formatter: CFNumberFormatter!, _ formatString: CFString!)
```

#### Discussion

The format string may override other properties previously set using other functions. If this function is not called, the default value of the format string is derived from the number formatter’s style.

## Parameters

- `formatter`: The number formatter to modify.
- `formatString`: The format string to be used by  . See   for more information.

## See Also

- [func CFNumberFormatterSetProperty(CFNumberFormatter!, CFNumberFormatterKey!, CFTypeRef!)](cfnumberformattersetproperty(_:_:_:).md)
  Sets a number formatter property using a key-value pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattersetformat(_:_:))*