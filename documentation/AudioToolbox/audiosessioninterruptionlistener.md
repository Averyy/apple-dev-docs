# AudioSessionInterruptionListener

**Framework**: Audio Toolbox  
**Kind**: typealias

Invoked when an audio interruption in iOS begins or ends.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioSessionInterruptionListener = (UnsafeMutableRawPointer?, UInt32) -> Void
```

#### Discussion

If you named your function `MyInterruptionListener`, you would declare it like this:

##### Discussion

To register your interruption listener callback with your application’s audio session object, specify it in the [`AudioSessionInitialize(_:_:_:_:)`](audiosessioninitialize(_:_:_:_:).md) function.

## Parameters

- `inClientData`: Data that you specified in the `inClientData` parameter of the [`AudioSessionInitialize(_:_:_:_:)`](audiosessioninitialize(_:_:_:_:).md) function. Can be `NULL`.
- `inInterruptionState`: A constant that indicates whether the interruption has just started or just ended. See [`Audio Session Interruption States`](1618425-audio-session-interruption-state.md).

## See Also

- [typealias AudioSessionPropertyListener](audiosessionpropertylistener.md)
  Invoked when an audio session property changes in iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiosessioninterruptionlistener)*