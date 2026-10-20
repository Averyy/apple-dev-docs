# NSSoundDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by delegates of [`NSSound`](./nssound.md) objects.

**Availability**:
- macOS

## Declaration

```swift
protocol NSSoundDelegate : NSObjectProtocol
```

```objc
@protocol NSSoundDelegate <NSObject>
```

## Topics

### Playing Sounds
- [func sound(NSSound, didFinishPlaying: Bool)](./nssounddelegate/sound%28_,didfinishplaying%29.md)
  This delegate method is called when an `NSSound` instance has completed playback of its sound data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Detecting When a Sound Finishes Playing
- [var delegate: (any NSSoundDelegate)?](./nssound/delegate.md)
  The sound’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssounddelegate)*