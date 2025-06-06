# playPattern(from:)

**Framework**: Core Haptics  
**Kind**: method

Plays a pattern that’s defined in a file at the specified URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func playPattern(from fileURL: URL) throws
```

#### Discussion

Start the engine prior to calling this method to provide low-latency playback. If the engine isn’t already running when you call this method, the system starts it, which can result in a significant playback delay.

## Parameters

- `fileURL`: The URL to the AHAP file containing the haptic event dictionary.

## See Also

- [func playPattern(from: Data) throws](chhapticengine/playpattern(from:)-7u8se.md)
  Plays a pattern from the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/playpattern(from:)-6m9m5)*