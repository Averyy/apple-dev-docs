# isEnabled

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether this capture event interaction is in an enabled state.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

Set this value to `false` when your app can’t or won’t respond to the action callbacks to avoid non-interactive buttons or UI elements.

## See Also

- [class var defaultCaptureSoundDisabled: Bool](avcaptureeventinteraction/defaultcapturesounddisabled.md)
  A Boolean value that indicates whether the default sound is in a disabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/isenabled)*