# init(element:fromBytes:timestamp:)

**Framework**: Core HID  
**Kind**: init

Creates a value for an HID element.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(element: HIDElement, fromBytes: Data, timestamp: SuspendingClock.Instant)
```

#### Discussion

The created value can be used to send a request to the associated device to update it’s current value for the element using [`HIDDeviceClient.ProvideElementUpdate`](hiddeviceclient/provideelementupdate.md).

## Parameters

- `element`: The element associated with this data.
- `fromBytes`: The data as an array of bytes.
- `timestamp`: The time that the value was created.

## See Also

- [init?<FloatingPointType>(element: HIDElement, fromPhysicalValue: FloatingPointType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromphysicalvalue:timestamp:).md)
  Creates a HID element value from a physical value.
- [init?<IntegerType>(element: HIDElement, fromLogicalValueTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromlogicalvaluetruncatingifneeded:timestamp:).md)
  Creates a HID element value from a logical value.
- [init<IntegerType>(element: HIDElement, fromIntegerTruncatingIfNeeded: IntegerType, timestamp: SuspendingClock.Instant)](hidelement/value/init(element:fromintegertruncatingifneeded:timestamp:).md)
  Creates an HID element value from an integer.
- [var element: HIDElement](hidelement/value/element.md)
  The [`HIDElement`](hidelement.md) associated with this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/init(element:frombytes:timestamp:))*