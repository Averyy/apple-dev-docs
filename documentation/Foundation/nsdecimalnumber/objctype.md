# objCType

**Framework**: Foundation  
**Kind**: property

A C string containing the Objective-C type for the data contained in the decimal number object.

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
var objCType: UnsafePointer<CChar> { get }
```

#### Discussion

For a decimal number object, this property always contains “d” (for double).

## See Also

- [var decimalValue: Decimal](nsdecimalnumber/decimalvalue.md)
  The decimal number’s value, expressed as an [`Decimal`](decimal.md) structure.
- [var doubleValue: Double](nsdecimalnumber/doublevalue.md)
  The decimal number’s closest approximate `double` value.
- [func description(withLocale: Any?) -> String](nsdecimalnumber/description(withlocale:).md)
  Returns a string representation of the decimal number appropriate for the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/objctype)*