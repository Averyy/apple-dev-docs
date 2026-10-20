# element

**Framework**: Core HID  
**Kind**: property  
**Role**: Instance Property

The [`HIDElement`](../../hidelement.md) associated with this value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var element: HIDElement
```

## See Also

### Create a HID element from a value
- [init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)](./init%28element,frombytes,timestamp%29.md)
  Creates a value for an HID element.
- [init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant)](./init%28element,fromphysicalvalue,timestamp%29.md)
  Creates a HID element value from a physical value.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](./init%28element,fromlogicalvaluetruncatingifneeded,timestamp%29.md)
  Creates a HID element value from a logical value.
- [init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](./init%28element,fromintegertruncatingifneeded,timestamp%29.md)
  Creates an HID element value from an integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/element)*