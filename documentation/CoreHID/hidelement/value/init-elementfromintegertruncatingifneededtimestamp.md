# init(element:fromIntegerTruncatingIfNeeded:timestamp:)

**Framework**: Core HID  
**Kind**: init

Creates an HID element value from an integer.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant) where IntegerType : FixedWidthInteger
```

#### Discussion

The logical and physical values are calculated, but don’t need to be valid.

## Parameters

- `element`: The element associated with this value.
- `fromIntegerTruncatingIfNeeded`: An integer to use for the value’s  , truncating or extending the bytes as necessary.
- `timestamp`: The time that the value was created.

## See Also

- [init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:frombytes:timestamp:).md)
  Creates a value for an HID element.
- [init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromphysicalvalue:timestamp:).md)
  Creates a HID element value from a physical value.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromlogicalvaluetruncatingifneeded:timestamp:).md)
  Creates a HID element value from a logical value.
- [var element: HIDElement](hidelement/value/element.md)
  The [`HIDElement`](hidelement.md) associated with this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/init(element:fromintegertruncatingifneeded:timestamp:))*