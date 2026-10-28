# decimalValue

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number object’s value expressed as an [`Decimal`](../decimal.md) structure.

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
var decimalValue: Decimal { get }
```

```objc
@property (readonly) NSDecimal decimalValue;
```

## Discussion

The [`Decimal`](../decimal.md) value isn’t guaranteed to be exact for `float` and `double` values.

## See Also

### Accessing Numeric Values
- [var boolValue: Bool](./boolvalue.md)
  The number object’s value expressed as a Boolean value.
- [var int8Value: CChar](./int8value.md)
  The number object’s value expressed as a `char`.
- [var doubleValue: Double](./doublevalue.md)
  The number object’s value expressed as a `double`, converted as necessary.
- [var floatValue: Float](./floatvalue.md)
  The number object’s value expressed as a `float`, converted as necessary.
- [var int32Value: Int32](./int32value.md)
  The number object’s value expressed as an `int`, converted as necessary.
- [var intValue: Int](./intvalue-95zzp.md)
  The number object’s value expressed as an `NSInteger` object, converted as necessary.
- [var int64Value: Int64](./int64value.md)
  The number object’s value expressed as a `long long`, converted as necessary.
- [var int16Value: Int16](./int16value.md)
  The number object’s value expressed as a `short`, converted as necessary.
- [var uint8Value: UInt8](./uint8value.md)
  The number object’s value expressed as an unsigned `char`, converted as necessary.
- [var uintValue: UInt](./uintvalue.md)
  The number object’s value expressed as an `NSUInteger` object, converted as necessary.
- [var uint32Value: UInt32](./uint32value.md)
  The number object’s value expressed as an unsigned `int`, converted as necessary.
- [var uint64Value: UInt64](./uint64value.md)
  The number object’s value expressed as an unsigned `long long`, converted as necessary.
- [var uint16Value: UInt16](./uint16value.md)
  The number object’s value expressed as an unsigned `short`, converted as necessary.
- [longValue](./longvalue.md)
  The number object’s value expressed as a `long`, converted as necessary.
- [unsignedLongValue](./unsignedlongvalue.md)
  The number object’s value expressed as an unsigned `long`, converted as necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnumber/decimalvalue)*