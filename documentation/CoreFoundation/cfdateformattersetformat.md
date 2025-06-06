# CFDateFormatterSetFormat(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the format string of the given date formatter to the specified value.

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
func CFDateFormatterSetFormat(_ formatter: CFDateFormatter!, _ formatString: CFString!)
```

#### Discussion

The format string may override other properties previously set using other functions. If this function is not called, the default value of the format string is derived from the date formatter’s date and time styles.

## Parameters

- `formatter`: The date formatter to modify.
- `formatString`: The format string for  . The syntax of this string is defined by  ..

## See Also

- [func CFDateFormatterSetProperty(CFDateFormatter!, CFString!, CFTypeRef!)](cfdateformattersetproperty(_:_:_:).md)
  Sets a date formatter property using a key-value pair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattersetformat(_:_:))*