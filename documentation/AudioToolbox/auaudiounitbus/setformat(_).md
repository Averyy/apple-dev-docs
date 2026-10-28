# setFormat(_:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Sets the bus’s audio format.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setFormat(_ format: AVAudioFormat) throws
```

```objc
- (BOOL) setFormat:(AVAudioFormat *) format error:(NSError **) outError;
```

## Discussion

- [`false`](../../Swift/false.md) if the operation failed.

## Discussion

Audio units can generally be expected to support the [`AVAudioFormat`](../../AVFAudio/avaudioformat.md) standard format (deinterleaved 32-bit float), at any sample rate.

Channel counts can be more complex. See the [`channelCapabilities`](../auaudiounit/channelcapabilities.md) reference for a more complete discussion.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `format`: The desired audio format.

## See Also

### Bus Methods and Properties
- [var format: AVAudioFormat](./format.md)
  The audio format and channel layout of audio being transferred on the bus.
- [var isEnabled: Bool](./isenabled.md)
  Determines whether the bus is active.
- [var name: String?](./name.md)
  A name for the bus.
- [var index: Int](./index.md)
  The index of this bus in its containing array.
- [var busType: AUAudioUnitBusType](./bustype.md)
  The bus type.
- [var ownerAudioUnit: AUAudioUnit](./owneraudiounit.md)
  The audio unit that owns the bus.
- [var supportedChannelLayoutTags: [NSNumber]?](./supportedchannellayouttags.md)
  An array of audio channel layout tags.
- [var contextPresentationLatency: TimeInterval](./contextpresentationlatency.md)
  Information about latency in the audio unit’s processing context.
- [var shouldAllocateBuffer: Bool](./shouldallocatebuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/setformat(_:))*