# AudioSessionPropertyListener

**Framework**: Audio Toolbox  
**Kind**: typealias

Invoked when an audio session property changes in iOS.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioSessionPropertyListener = (UnsafeMutableRawPointer?, AudioSessionPropertyID, UInt32, UnsafeRawPointer?) -> Void
```

#### Discussion

If you named your function `MyPropertyListener`, you would declare it like this:

##### Discussion

You can register one or more property listener callbacks with your application’s audio session object by calling the [`AudioSessionAddPropertyListener(_:_:_:)`](audiosessionaddpropertylistener(_:_:_:).md) function.

## Parameters

- `inClientData`: Data that you specified in the `inClientData` parameter of the [`AudioSessionAddPropertyListener(_:_:_:)`](audiosessionaddpropertylistener(_:_:_:).md) function. Can be `NULL`.
- `inID`: The identifier for the audio session property whose value just changed. See [`Audio Session Property Identifiers`](1618455-audio-session-property-identifie.md).
- `inDataSize`: The size, in bytes, of the value of the changed property.
- `inData`: The new value of the changed property.

## See Also

- [typealias AudioSessionInterruptionListener](audiosessioninterruptionlistener.md)
  Invoked when an audio interruption in iOS begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiosessionpropertylistener)*