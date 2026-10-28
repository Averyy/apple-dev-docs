# description(withLocale:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) descriptionWithLocale:(id) locale;
```

## Discussion

This is a convenience method for calling the [`NSDecimalString(_:_:)`](../nsdecimalstring%28_,_%29.md) function.

## Parameters

- `locale`: Either an instance of [`NSLocale`](../nslocale.md) or a dictionary with a string value corresponding to the [`decimalSeparator`](../nslocale/key/decimalseparator.md) key.

## See Also

### Accessing the Value
- [var decimalValue: Decimal](./decimalvalue.md)
  The decimal number’s value, expressed as an [`Decimal`](../decimal.md) structure.
- [var doubleValue: Double](./doublevalue.md)
  The decimal number’s closest approximate `double` value.
- [var objCType: UnsafePointer<CChar>](./objctype.md)
  A C string containing the Objective-C type for the data contained in the decimal number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalnumber/description(withlocale:))*