# init(format:)

**Framework**: Audio Toolbox  
**Kind**: init  
**Role**: Initializer

Initializes a bus object with a specific format.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
init(format: AVAudioFormat) throws
```

```objc
- (instancetype) initWithFormat:(AVAudioFormat *) format error:(NSError **) outError;
```

## Return Value

A newly-initialized bus object, or `nil` if the operation failed.

## Discussion

Audio units can generally be expected to support the [`AVAudioFormat`](../../AVFAudio/avaudioformat.md) standard format (deinterleaved 32-bit float), at any sample rate.

Channel counts can be more complex. See the [`channelCapabilities`](../auaudiounit/channelcapabilities.md) reference for a more complete discussion.

Initialization will fail and return an error if the specified format is unsupported for the bus.

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `format`: The initial audio format.

## See Also

### Audio Unit Implementations
- [var supportedChannelCounts: [NSNumber]?](./supportedchannelcounts.md)
  An array of numbers indicating the supported number of channels for this bus.
- [var maximumChannelCount: AUAudioChannelCount](./maximumchannelcount.md)
  The maximum number of channels supported for this bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitbus/init(format:))*