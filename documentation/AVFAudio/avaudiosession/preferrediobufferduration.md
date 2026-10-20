# preferredIOBufferDuration

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSTimeInterval preferredIOBufferDuration;
```

#### Discussion

The value of this property indicates the buffer duration selected using the [`setPreferredIOBufferDuration(_:)`](./setpreferrediobufferduration%28_%29.md) method.

To determine the actual buffer duration, query the [`ioBufferDuration`](./iobufferduration.md) property.

## See Also

### Configuring I/O buffer duration
- [var ioBufferDuration: TimeInterval](./iobufferduration.md)
  The current I/O buffer duration, in seconds.
- [func setPreferredIOBufferDuration(TimeInterval) throws](./setpreferrediobufferduration%28_%29.md)
  Sets the preferred audio I/O buffer duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferrediobufferduration)*