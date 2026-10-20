# AudioSessionInterruptionListener

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Invoked when an audio interruption in iOS begins or ends.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
typealias AudioSessionInterruptionListener = (UnsafeMutableRawPointer?, UInt32) -> Void
```

```c
typedef void (*)(void *, unsigned int) AudioSessionInterruptionListener;
```

#### Discussion

If you named your function `MyInterruptionListener`, you would declare it like this:

##### Discussion

To register your interruption listener callback with your application’s audio session object, specify it in the [`AudioSessionInitialize(_:_:_:_:)`](./audiosessioninitialize%28_,_,_,_%29.md) function.

## Parameters

- `inClientData`: Data that you specified in the `inClientData` parameter of the [`AudioSessionInitialize(_:_:_:_:)`](./audiosessioninitialize%28_,_,_,_%29.md) function. Can be `NULL`.
- `inInterruptionState`: A constant that indicates whether the interruption has just started or just ended. See [Audio Session Interruption States](./api-1618425-audio-session-interruption-state.md).

## See Also

### Callbacks
- [typealias AudioSessionPropertyListener](./audiosessionpropertylistener.md)
  Invoked when an audio session property changes in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiosessioninterruptionlistener)*