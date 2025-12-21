# shouldRandomizeStartTime

**Framework**: RealityKit  
**Kind**: property

Stores a Boolean indicating whether the playback begins from the start of the file, or from a random position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var shouldRandomizeStartTime: Bool
```

#### Discussion

When this property and [`shouldLoop`](audiofileresource/configuration-swift.struct/shouldloop.md) are both true, only the first playback iteration begins from a random position.

## See Also

- [var shouldLoop: Bool](audiofileresource/configuration-swift.struct/shouldloop.md)
  Stores a Boolean indicating whether the playback loops infinitely, until manually stopped or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiofileresource/configuration-swift.struct/shouldrandomizestarttime)*