# CFNumberFormatterSetProperty(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets a number formatter property using a key-value pair.

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
func CFNumberFormatterSetProperty(_ formatter: CFNumberFormatter!, _ key: CFNumberFormatterKey!, _ value: CFTypeRef!)
```

## Parameters

- `formatter`: The number formatter to modify.
- `key`: The name of the property of   to set. See   for a description of possible values.
- `value`: The value of the specified key. This must be an instance of the correct   object for the corresponding key.

## See Also

- [func CFNumberFormatterSetFormat(CFNumberFormatter!, CFString!)](cfnumberformattersetformat(_:_:).md)
  Sets the format string of a number formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattersetproperty(_:_:_:))*