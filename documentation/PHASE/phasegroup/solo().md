# solo()

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Silences all other groups.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func solo()
```

```objc
- (void) solo;
```

#### Discussion

The engine silences all groups other than the group on which the app calls this function.

## See Also

### Silencing Sounds
- [func mute()](./mute%28%29.md)
  Silences the group.
- [func unmute()](./unmute%28%29.md)
  Restores the group’s volume.
- [var isMuted: Bool](./ismuted.md)
  A Boolean value that indicates whether the app silences the group.
- [func unsolo()](./unsolo%28%29.md)
  Restores the other groups’ volume.
- [var isSoloed: Bool](./issoloed.md)
  A Boolean value that indicates whether the app silences all groups other than this group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegroup/solo())*