# description(withLocale:)

**Framework**: Foundation  
**Kind**: method

Returns a string representation of the decimal number appropriate for the specified locale.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func description(withLocale locale: Any?) -> String
```

#### Discussion

This is a convenience method for calling the [`NSDecimalString(_:_:)`](nsdecimalstring(_:_:).md) function.

## Parameters

- `locale`: Either an instance of   or a dictionary with a string value corresponding to the   key.

## See Also

- [var decimalValue: Decimal](nsdecimalnumber/decimalvalue.md)
  The decimal number’s value, expressed as an [`Decimal`](decimal.md) structure.
- [var doubleValue: Double](nsdecimalnumber/doublevalue.md)
  The decimal number’s closest approximate `double` value.
- [var objCType: UnsafePointer<CChar>](nsdecimalnumber/objctype.md)
  A C string containing the Objective-C type for the data contained in the decimal number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/description(withlocale:))*