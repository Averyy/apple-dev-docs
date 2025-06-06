# maximumChannelCount

**Framework**: Audio Toolbox  
**Kind**: property

The maximum number of channels supported for this bus.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var maximumChannelCount: AUAudioChannelCount { get set }
```

#### Discussion

If the value of [`supportedChannelCounts`](auaudiounitbus/supportedchannelcounts.md) is set, then this value is derived from it. If setting a new value on this property makes the current bus format unsupported, then the value of [`format`](auaudiounitbus/format.md) is set to `nil`.

The default value is `UINT_MAX`.

## See Also

- [init(format: AVAudioFormat) throws](auaudiounitbus/init(format:).md)
  Initializes a bus object with a specific format.
- [var supportedChannelCounts: [NSNumber]?](auaudiounitbus/supportedchannelcounts.md)
  An array of numbers indicating the supported number of channels for this bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/maximumchannelcount)*