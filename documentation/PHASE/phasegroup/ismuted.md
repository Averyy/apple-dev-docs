# isMuted

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app silences the group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isMuted: Bool { get }
```

```objc
@property (readonly, getter=isMuted) BOOL muted;
```

## See Also

### Silencing Sounds
- [func mute()](./mute%28%29.md)
  Silences the group.
- [func unmute()](./unmute%28%29.md)
  Restores the group’s volume.
- [func solo()](./solo%28%29.md)
  Silences all other groups.
- [func unsolo()](./unsolo%28%29.md)
  Restores the other groups’ volume.
- [var isSoloed: Bool](./issoloed.md)
  A Boolean value that indicates whether the app silences all groups other than this group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegroup/ismuted)*