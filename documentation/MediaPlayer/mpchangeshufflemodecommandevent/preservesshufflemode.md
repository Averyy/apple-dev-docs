# preservesShuffleMode

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the shuffle mode is preserved between playback sessions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var preservesShuffleMode: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL preservesShuffleMode;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the shuffle mode is preserved between playback sessions.

## See Also

### Changing the shuffle mode
- [var shuffleType: MPShuffleType](./shuffletype.md)
  The shuffle type used when fulfilling the event request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent/preservesshufflemode)*