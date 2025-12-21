# NetworkCompatibilityToken.Compatibility.sessionProtocolVersionMismatch

**Framework**: RealityKit  
**Kind**: case

An indication that two peers running incompatible versions of RealityKit can’t sync.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS ?+

## Declaration

```swift
case sessionProtocolVersionMismatch
```

#### Discussion

The [`compatibilityWith(_:)`](networkcompatibilitytoken/compatibilitywith(_:).md) method returns this value when two devices have different OS versions and there has been a significant change in networking protocol between those releases.

## See Also

- [NetworkCompatibilityToken.Compatibility.compatible](networkcompatibilitytoken/compatibility/compatible.md)
  An indication that the compared devices are running compatible versions of RealityKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/compatibility/sessionprotocolversionmismatch)*