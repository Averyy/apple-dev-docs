# valueDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The block that the axis element calls when its value changes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxis2DInput, GCPoint2) -> Void)? { get set }
```

```objc
@property (atomic, copy, nullable) void (^valueDidChangeHandler)(id<GCPhysicalInputElement>element, id<GCAxis2DInput>input, GCPoint2 value);
```

#### Discussion

The block’s parameters are:

- **`element`**: The element with the value that changes.
- **`input`**: The input on the element that changes.
- **`value`**: The value of the input when the element invokes this handler.

## See Also

### Getting the value
- [var value: GCPoint2](./value.md)
  The axis input represented as a normalized point in a two-dimensional coordinate system.
- [struct GCPoint2](../gcpoint2.md)
  A structure that represents a normalized point in a two-dimensional coordinate system.
- [var lastValueTimestamp: TimeInterval](./lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](./lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcaxis2dinput/valuedidchangehandler)*