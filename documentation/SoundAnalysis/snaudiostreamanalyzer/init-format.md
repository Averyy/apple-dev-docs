# init(format:)

**Framework**: Sound Analysis  
**Kind**: init

Creates a new audio stream analyzer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(format: AVAudioFormat)
```

#### Discussion

> ❗ **Important**:  The audio stream format must be a linear PCM (pulse code modulation).

 The audio stream format must be a linear PCM (pulse code modulation).

## Parameters

- `format`: The audio format of an audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer/init(format:))*