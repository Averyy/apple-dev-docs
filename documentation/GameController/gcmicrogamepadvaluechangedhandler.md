# GCMicroGamepadValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias  
**Role**: Type Alias

Signature for the block that this profile calls when an element’s value changes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCMicroGamepadValueChangedHandler = (GCMicroGamepad, GCControllerElement) -> Void
```

```c
typedef void (^)(GCMicroGamepad *, GCControllerElement *) GCMicroGamepadValueChangedHandler;
```

## Parameters

- `gamepad`: The profile whose element value changes.
- `element`: The element in the profile whose value changes.

## See Also

### Receiving a callback when input values change
- [var valueChangedHandler: GCMicroGamepadValueChangedHandler?](./gcmicrogamepad/valuechangedhandler.md)
  The block that this profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadvaluechangedhandler)*