# CFDateFormatterSetProperty(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets a date formatter property using a key-value pair.

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
func CFDateFormatterSetProperty(_ formatter: CFDateFormatter!, _ key: CFString!, _ value: CFTypeRef!)
```

```c
extern void CFDateFormatterSetProperty(CFDateFormatterRef formatter, CFStringRef key, CFTypeRef value);
```

## Parameters

- `formatter`: The date formatter to modify.
- `key`: The name of the property to set. See [Date Formatter Property Keys](./date-formatter-property-keys.md) for a description of possible values for this parameter.
- `value`: The value for `key`. This should be a CFType object corresponding to the specified key.

## See Also

### Configuring a Date Formatter
- [func CFDateFormatterSetFormat(CFDateFormatter!, CFString!)](./cfdateformattersetformat%28_,_%29.md)
  Sets the format string of the given date formatter to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformattersetproperty(_:_:_:))*