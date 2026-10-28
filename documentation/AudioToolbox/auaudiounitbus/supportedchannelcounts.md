# supportedChannelCounts

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

An array of numbers indicating the supported number of channels for this bus.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var supportedChannelCounts: [NSNumber]? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSArray<NSNumber *> * supportedChannelCounts;
```

## Discussion

If the value of this property is `nil`, then any number less than or equal to the value of [`maximumChannelCount`](./maximumchannelcount.md) is supported. If setting a new value on this property makes the current bus format unsupported, then the value of [`format`](./format.md) is set to `nil`.

The default value is `nil`.

## See Also

### Audio Unit Implementations
- [init(format: AVAudioFormat) throws](./init%28format%29.md)
  Initializes a bus object with a specific format.
- [var maximumChannelCount: AUAudioChannelCount](./maximumchannelcount.md)
  The maximum number of channels supported for this bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/supportedchannelcounts)*