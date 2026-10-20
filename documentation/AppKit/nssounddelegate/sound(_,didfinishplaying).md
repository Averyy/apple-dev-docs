# sound(_:didFinishPlaying:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This delegate method is called when an `NSSound` instance has completed playback of its sound data.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func sound(_ sound: NSSound, didFinishPlaying flag: Bool)
```

```objc
- (void) sound:(NSSound *) sound didFinishPlaying:(BOOL) flag;
```

## Parameters

- `sound`: The `NSSound` that has completed playback of its sound data.
- `flag`: [`true`](../../Swift/true.md) when playback was successful; [`false`](../../Swift/false.md) otherwise.

## See Also

### Related Documentation
- [Sound Programming Topics for Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sound/Sound.html#//apple_ref/doc/uid/10000104i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssounddelegate/sound(_:didfinishplaying:))*