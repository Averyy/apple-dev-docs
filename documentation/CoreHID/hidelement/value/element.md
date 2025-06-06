# element

**Framework**: Core HID  
**Kind**: property

The [`HIDElement`](hidelement.md) associated with this value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var element: HIDElement
```

## See Also

- [init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:frombytes:timestamp:).md)
  Creates a value for an HID element.
- [init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromphysicalvalue:timestamp:).md)
  Creates a HID element value from a physical value.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromlogicalvaluetruncatingifneeded:timestamp:).md)
  Creates a HID element value from a logical value.
- [init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromintegertruncatingifneeded:timestamp:).md)
  Creates an HID element value from an integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/element)*