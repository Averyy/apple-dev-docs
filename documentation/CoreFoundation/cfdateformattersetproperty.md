# CFDateFormatterSetProperty(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets a date formatter property using a key-value pair.

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
func CFDateFormatterSetProperty(_ formatter: CFDateFormatter!, _ key: CFString!, _ value: CFTypeRef!)
```

## Parameters

- `formatter`: The date formatter to modify.
- `key`: The name of the property to set. See   for a description of possible values for this parameter.
- `value`: The value for  . This should be a CFType object corresponding to the specified key.

## See Also

- [func CFDateFormatterSetFormat(CFDateFormatter!, CFString!)](cfdateformattersetformat(_:_:).md)
  Sets the format string of the given date formatter to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattersetproperty(_:_:_:))*