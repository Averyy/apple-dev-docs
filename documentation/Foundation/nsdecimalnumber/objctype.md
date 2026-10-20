# objCType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) const char * objCType;
```

#### Discussion

For a decimal number object, this property always contains “d” (for double).

## See Also

### Accessing the Value
- [var decimalValue: Decimal](./decimalvalue.md)
  The decimal number’s value, expressed as an [`Decimal`](../decimal.md) structure.
- [var doubleValue: Double](./doublevalue.md)
  The decimal number’s closest approximate `double` value.
- [func description(withLocale: Any?) -> String](./description%28withlocale%29.md)
  Returns a string representation of the decimal number appropriate for the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/objctype)*