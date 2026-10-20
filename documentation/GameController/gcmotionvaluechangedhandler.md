# GCMotionValueChangedHandler

**Framework**: Game Controller  
**Kind**: typealias  
**Role**: Type Alias

The signature for the block that the profile calls when an element’s value changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias GCMotionValueChangedHandler = (GCMotion) -> Void
```

```c
typedef void (^)(GCMotion *) GCMotionValueChangedHandler;
```

## Parameters

- `motion`: The profile with the element values that change.

## See Also

### Receiving a Callback When Input Values Change
- [var valueChangedHandler: GCMotionValueChangedHandler?](./gcmotion/valuechangedhandler.md)
  The block that the profile calls when an element’s value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotionvaluechangedhandler)*