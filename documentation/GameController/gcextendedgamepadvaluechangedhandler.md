# GCExtendedGamepadValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias  
**Role**: Type Alias

The signature for the block that the profile calls when an element’s value changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCExtendedGamepadValueChangedHandler = (GCExtendedGamepad, GCControllerElement) -> Void
```

```c
typedef void (^)(GCExtendedGamepad *, GCControllerElement *) GCExtendedGamepadValueChangedHandler;
```

## Parameters

- `gamepad`: The profile with the element value that changes.
- `element`: The element with the value that changes in the profile.

## See Also

### Getting change information
- [var valueChangedHandler: GCExtendedGamepadValueChangedHandler?](./gcextendedgamepad/valuechangedhandler.md)
  The block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadvaluechangedhandler)*