# AudioSessionPropertyListener

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

Invoked when an audio session property changes in iOS.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
typealias AudioSessionPropertyListener = (UnsafeMutableRawPointer?, AudioSessionPropertyID, UInt32, UnsafeRawPointer?) -> Void
```

```c
typedef void (*)(void *, unsigned int, unsigned int, const void *) AudioSessionPropertyListener;
```

## Discussion

If you named your function `MyPropertyListener`, you would declare it like this:

### Discussion

You can register one or more property listener callbacks with your application’s audio session object by calling the [`AudioSessionAddPropertyListener(_:_:_:)`](./audiosessionaddpropertylistener%28_,_,_%29.md) function.

## Parameters

- `inClientData`: Data that you specified in the `inClientData` parameter of the [`AudioSessionAddPropertyListener(_:_:_:)`](./audiosessionaddpropertylistener%28_,_,_%29.md) function. Can be `NULL`.
- `inID`: The identifier for the audio session property whose value just changed. See [Audio Session Property Identifiers](./api-1618455-audio-session-property-identifie.md).
- `inDataSize`: The size, in bytes, of the value of the changed property.
- `inData`: The new value of the changed property.

## See Also

### Callbacks
- [typealias AudioSessionInterruptionListener](./audiosessioninterruptionlistener.md)
  Invoked when an audio interruption in iOS begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiosessionpropertylistener)*