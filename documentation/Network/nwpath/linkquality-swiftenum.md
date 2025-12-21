# NWPath.LinkQuality

**Framework**: Network  
**Kind**: enum

Represents the link quality measurement of the link layer network attachment

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum LinkQuality
```

#### Overview

Use this value to tune initial values for algorithms that can scale with the capabilities of the network. Do not use this value to gate connection attempts or to override adjustments that would be made based on actual network performance.

## Topics

### Enumeration Cases
- [NWPath.LinkQuality.good](nwpath/linkquality-swift.enum/good.md)
  Link quality is good
- [NWPath.LinkQuality.minimal](nwpath/linkquality-swift.enum/minimal.md)
  Link quality is minimal
- [NWPath.LinkQuality.moderate](nwpath/linkquality-swift.enum/moderate.md)
  Link quality is moderate
- [NWPath.LinkQuality.unknown](nwpath/linkquality-swift.enum/unknown.md)
  No link quality measurement is available

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwpath/linkquality-swift.enum)*