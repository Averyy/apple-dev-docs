# valueDidChangeHandler

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The block that the profile calls when an element’s value changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCLinearInput, Float) -> Void)? { get set }
```

```objc
@property (atomic, copy, nullable) void (^valueDidChangeHandler)(id<GCPhysicalInputElement>element, id<GCLinearInput>input, float value);
```

## Discussion

The block’s parameters are:

- **element**: The element whose value changed.
- **input**: The input object that changed.
- **value**: The value of the input at the time the input object calls this handler.

## See Also

### Getting the value
- [var value: Float](./value.md)
  The value in unit coordinates.
- [var lastValueTimestamp: TimeInterval](./lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](./lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gclinearinput/valuedidchangehandler)*