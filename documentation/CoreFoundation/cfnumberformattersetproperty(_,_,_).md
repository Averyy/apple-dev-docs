# CFNumberFormatterSetProperty(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets a number formatter property using a key-value pair.

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
func CFNumberFormatterSetProperty(_ formatter: CFNumberFormatter!, _ key: CFNumberFormatterKey!, _ value: CFTypeRef!)
```

```c
extern void CFNumberFormatterSetProperty(CFNumberFormatterRef formatter, CFNumberFormatterKey key, CFTypeRef value);
```

## Parameters

- `formatter`: The number formatter to modify.
- `key`: The name of the property of `formatter` to set. See [Number Formatter Property Keys](./number-formatter-property-keys.md) for a description of possible values.
- `value`: The value of the specified key. This must be an instance of the correct `CFType` object for the corresponding key.

## See Also

### Configuring a Number Formatter
- [func CFNumberFormatterSetFormat(CFNumberFormatter!, CFString!)](./cfnumberformattersetformat%28_,_%29.md)
  Sets the format string of a number formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformattersetproperty(_:_:_:))*