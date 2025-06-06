# AVVideoH264EntropyModeKey

**Framework**: AVFoundation  
**Kind**: var

The entropy encoding mode for H.264 compression.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let AVVideoH264EntropyModeKey: String
```

#### Discussion

This property controls whether an H.264 encoder uses [`AVVideoH264EntropyModeCAVLC`](avvideoh264entropymodecavlc.md) or [`AVVideoH264EntropyModeCABAC`](avvideoh264entropymodecabac.md). CABAC generally gives better compression at the expense of higher computational overhead.

> ❗ **Important**:  The default value is encoder-specific and may change depending on other encoder settings. Set a value for this property only if the requested profile and level support it. Setting an incompatible value may result in encoding errors or a noncompliant output stream.

 The default value is encoder-specific and may change depending on other encoder settings. Set a value for this property only if the requested profile and level support it. Setting an incompatible value may result in encoding errors or a noncompliant output stream.

## See Also

- [let AVVideoH264EntropyModeCABAC: String](avvideoh264entropymodecabac.md)
  The encoder uses Context-based Adaptive Binary Arithmetic Coding.
- [let AVVideoH264EntropyModeCAVLC: String](avvideoh264entropymodecavlc.md)
  The encoder uses Context-based Adaptive Variable Length Coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoh264entropymodekey)*