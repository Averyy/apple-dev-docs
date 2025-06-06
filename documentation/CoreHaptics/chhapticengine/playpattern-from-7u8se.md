# playPattern(from:)

**Framework**: Core Haptics  
**Kind**: method

Plays a pattern from the specified data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func playPattern(from data: Data) throws
```

#### Discussion

Start the engine prior to calling this method to provide low-latency playback. If the engine isn’t already running when you call this method, the system starts it, which can result in a significant playback delay.

## Parameters

- `data`: The raw data containing the haptic pattern, structured as an AHAP dictionary.

## See Also

- [func playPattern(from: URL) throws](chhapticengine/playpattern(from:)-6m9m5.md)
  Plays a pattern that’s defined in a file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/playpattern(from:)-7u8se)*