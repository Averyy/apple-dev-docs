# NSSoundDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods implemented by delegates of [`NSSound`](nssound.md) objects.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSSoundDelegate : NSObjectProtocol
```

## Topics

### Playing Sounds
- [func sound(NSSound, didFinishPlaying: Bool)](nssounddelegate/sound(_:didfinishplaying:).md)
  This delegate method is called when an `NSSound` instance has completed playback of its sound data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSSoundDelegate)?](nssound/delegate.md)
  The sound’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssounddelegate)*