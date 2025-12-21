# defaultCaptureSoundDisabled

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether the default sound is in a disabled state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@MainActor
class var defaultCaptureSoundDisabled: Bool { get set }
```

#### Discussion

If `true`, you must handle sound playback for capture events manually using the [`play(_:)`](avcaptureevent/play(_:).md) method.

> ❗ **Important**: To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## See Also

- [var isEnabled: Bool](avcaptureeventinteraction/isenabled.md)
  A Boolean value that indicates whether this capture event interaction is in an enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/defaultcapturesounddisabled)*