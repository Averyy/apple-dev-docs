# init(element:fromPhysicalValue:timestamp:)

**Framework**: Core HID  
**Kind**: init  
**Role**: Initializer

Creates a HID element value from a physical value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant) where FloatingPointType : BinaryFloatingPoint
```

#### Discussion

The raw value and physical value are calculated; both must be valid.

## Parameters

- `element`: The element associated with this value.
- `timestamp`: The time that the value was created.

## See Also

### Create a HID element from a value
- [init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)](./init%28element,frombytes,timestamp%29.md)
  Creates a value for an HID element.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](./init%28element,fromlogicalvaluetruncatingifneeded,timestamp%29.md)
  Creates a HID element value from a logical value.
- [init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](./init%28element,fromintegertruncatingifneeded,timestamp%29.md)
  Creates an HID element value from an integer.
- [var element: HIDElement](./element.md)
  The [`HIDElement`](../../hidelement.md) associated with this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/init(element:fromphysicalvalue:timestamp:))*