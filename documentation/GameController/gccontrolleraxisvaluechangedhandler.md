# GCControllerAxisValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias  
**Role**: Type Alias

The signature for the block that executes when the user changes the axis value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCControllerAxisValueChangedHandler = (GCControllerAxisInput, Float) -> Void
```

```c
typedef void (^)(GCControllerAxisInput *, float) GCControllerAxisValueChangedHandler;
```

## Parameters

- `axis`: The axis that the user changed.
- `value`: A normalized value for the axis ranging from `-1` to `1`.

## See Also

### Getting change information
- [var valueChangedHandler: GCControllerAxisValueChangedHandler?](./gccontrolleraxisinput/valuechangedhandler.md)
  The block that the element calls when the user changes the axis value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrolleraxisvaluechangedhandler)*