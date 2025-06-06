# preferredIOBufferDuration

**Framework**: AVFAudio  
**Kind**: property

The preferred I/O buffer duration, in seconds.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredIOBufferDuration: TimeInterval { get }
```

#### Discussion

The value of this property indicates the buffer duration selected using the [`setPreferredIOBufferDuration(_:)`](avaudiosession/setpreferrediobufferduration(_:).md) method.

To determine the actual buffer duration, query the [`ioBufferDuration`](avaudiosession/iobufferduration.md) property.

## See Also

- [var ioBufferDuration: TimeInterval](avaudiosession/iobufferduration.md)
  The current I/O buffer duration, in seconds.
- [func setPreferredIOBufferDuration(TimeInterval) throws](avaudiosession/setpreferrediobufferduration(_:).md)
  Sets the preferred audio I/O buffer duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferrediobufferduration)*