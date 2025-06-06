# supportedChannelCounts

**Framework**: Audio Toolbox  
**Kind**: property

An array of numbers indicating the supported number of channels for this bus.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var supportedChannelCounts: [NSNumber]? { get set }
```

#### Discussion

If the value of this property is `nil`, then any number less than or equal to the value of [`maximumChannelCount`](auaudiounitbus/maximumchannelcount.md) is supported. If setting a new value on this property makes the current bus format unsupported, then the value of [`format`](auaudiounitbus/format.md) is set to `nil`.

The default value is `nil`.

## See Also

- [init(format: AVAudioFormat) throws](auaudiounitbus/init(format:).md)
  Initializes a bus object with a specific format.
- [var maximumChannelCount: AUAudioChannelCount](auaudiounitbus/maximumchannelcount.md)
  The maximum number of channels supported for this bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/supportedchannelcounts)*