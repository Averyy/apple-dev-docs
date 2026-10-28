# doubleValue

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The decimal number’s closest approximate `double` value.

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
var doubleValue: Double { get }
```

```objc
@property (readonly) double doubleValue;
```

## Discussion

Not all decimal numbers can be accurately represented using a `double` value.

## See Also

### Accessing the Value
- [var decimalValue: Decimal](./decimalvalue.md)
  The decimal number’s value, expressed as an [`Decimal`](../decimal.md) structure.
- [func description(withLocale: Any?) -> String](./description%28withlocale%29.md)
  Returns a string representation of the decimal number appropriate for the specified locale.
- [var objCType: UnsafePointer<CChar>](./objctype.md)
  A C string containing the Objective-C type for the data contained in the decimal number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/doublevalue)*