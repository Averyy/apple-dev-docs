# AudioBalanceFadeType.equalPower

**Framework**: Audio Toolbox  
**Kind**: case

Overall loudness remains constant, but gain can exceed 1.0. The gain value is 1.0 when the balance and fade are in the center. From there they can increase to +3dB (1.414) and decrease to silence.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case equalPower
```

## See Also

- [AudioBalanceFadeType.maxUnityGain](audiobalancefadetype/maxunitygain.md)
  Ensures that the overall gain value never exceeds 1.0 by fading one channel as the other channel’s level rises. This can reduce overall loudness when the balance or fade is not in the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiobalancefadetype/equalpower)*