# lastValueLatency

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The time in seconds between the last value change and the current time.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

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
- [var value: Float](./value.md)
  The value in unit coordinates.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCLinearInput, Float) -> Void)?](./valuedidchangehandler.md)
  The block that the profile calls when an element’s value changes.
- [var lastValueTimestamp: TimeInterval](./lastvaluetimestamp.md)
  The time of the most recent value change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gclinearinput/lastvaluelatency)*