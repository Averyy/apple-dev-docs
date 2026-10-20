# lastValueLatency

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The time in seconds between the last value change and the current time.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var lastValueLatency: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval lastValueLatency;
```

#### Discussion

Use this property as a minimum latency value that may not include latency that accrues on the device or when it transmits the event.

## See Also

### Getting the value
- [var value: GCPoint2](./value.md)
  The axis input represented as a normalized point in a two-dimensional coordinate system.
- [struct GCPoint2](../gcpoint2.md)
  A structure that represents a normalized point in a two-dimensional coordinate system.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxis2DInput, GCPoint2) -> Void)?](./valuedidchangehandler.md)
  The block that the axis element calls when its value changes.
- [var lastValueTimestamp: TimeInterval](./lastvaluetimestamp.md)
  The time of the most recent value change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxis2dinput/lastvaluelatency)*