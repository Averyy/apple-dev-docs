# sound(_:didFinishPlaying:)

**Framework**: AppKit  
**Kind**: method

This delegate method is called when an `NSSound` instance has completed playback of its sound data.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func sound(_ sound: NSSound, didFinishPlaying flag: Bool)
```

## Parameters

- `sound`: The   that has completed playback of its sound data.
- `flag`:   when playback was successful;   otherwise.

## See Also

- [Sound Programming Topics for Cocoa](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sound/Sound.html#//apple_ref/doc/uid/10000104i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssounddelegate/sound(_:didfinishplaying:))*