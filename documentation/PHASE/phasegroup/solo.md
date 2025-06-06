# solo()

**Framework**: PHASE  
**Kind**: method

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

#### Discussion

The engine silences all groups other than the group on which the app calls this function.

## See Also

- [func mute()](phasegroup/mute.md)
  Silences the group.
- [func unmute()](phasegroup/unmute.md)
  Restores the group’s volume.
- [var isMuted: Bool](phasegroup/ismuted.md)
  A Boolean value that indicates whether the app silences the group.
- [func unsolo()](phasegroup/unsolo.md)
  Restores the other groups’ volume.
- [var isSoloed: Bool](phasegroup/issoloed.md)
  A Boolean value that indicates whether the app silences all groups other than this group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegroup/solo())*