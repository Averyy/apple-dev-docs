# ioBufferDuration

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The current I/O buffer duration, in seconds.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var ioBufferDuration: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval IOBufferDuration;
```

## See Also

### Configuring I/O buffer duration
- [var preferredIOBufferDuration: TimeInterval](./preferrediobufferduration.md)
  The preferred I/O buffer duration, in seconds.
- [func setPreferredIOBufferDuration(TimeInterval) throws](./setpreferrediobufferduration%28_%29.md)
  Sets the preferred audio I/O buffer duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/iobufferduration)*