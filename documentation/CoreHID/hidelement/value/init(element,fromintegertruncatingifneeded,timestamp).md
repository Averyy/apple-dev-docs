# init(element:fromIntegerTruncatingIfNeeded:timestamp:)

**Framework**: Core HID  
**Kind**: init  
**Role**: Initializer

Creates an HID element value from an integer.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant) where IntegerType : FixedWidthInteger
```

## Discussion

The logical and physical values are calculated, but don’t need to be valid.

## Parameters

- `element`: The element associated with this value.
- `fromIntegerTruncatingIfNeeded`: An integer to use for the value’s [`bytes`](./bytes.md), truncating or extending the bytes as necessary.
- `timestamp`: The time that the value was created.

## See Also

### Create a HID element from a value
- [init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)](./init%28element,frombytes,timestamp%29.md)
  Creates a value for an HID element.
- [init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant)](./init%28element,fromphysicalvalue,timestamp%29.md)
  Creates a HID element value from a physical value.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](./init%28element,fromlogicalvaluetruncatingifneeded,timestamp%29.md)
  Creates a HID element value from a logical value.
- [var element: HIDElement](./element.md)
  The [`HIDElement`](../../hidelement.md) associated with this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/init(element:fromintegertruncatingifneeded:timestamp:))*