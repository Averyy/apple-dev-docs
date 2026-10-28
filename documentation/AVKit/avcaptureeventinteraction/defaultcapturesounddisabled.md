# defaultCaptureSoundDisabled

**Framework**: AVKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the default sound is in a disabled state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var defaultCaptureSoundDisabled: Bool { get set }
```

```objc
@property (class, nonatomic, readwrite) BOOL defaultCaptureSoundDisabled;
```

## Discussion

If `true`, you must handle sound playback for capture events manually using the [`play(_:)`](../avcaptureevent/play%28_%29.md) method.

> ❗ **Important**: To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## See Also

### Inspecting the interaction
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether this capture event interaction is in an enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/defaultcapturesounddisabled)*