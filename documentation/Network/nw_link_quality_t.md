# nw_link_quality_t

**Framework**: Network  
**Kind**: struct

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct nw_link_quality_t
```

#### Overview

Link quality measurement is a representation of the expected capabilities of the link layer network attachment. Use this value to tune initial values for algorithms that can scale with the capabilities of the network. Do not use this value to gate connection attempts or to override adjustments that would be made based on actual network performance.

## Topics

### Initializers
- [init(UInt8)](nw_link_quality_t/init(_:).md)
- [init(rawValue: UInt8)](nw_link_quality_t/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt8](nw_link_quality_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_link_quality_t)*