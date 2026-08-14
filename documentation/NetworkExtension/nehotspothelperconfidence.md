# NEHotspotHelperConfidence

**Framework**: Network Extension  
**Kind**: enum

A type that indicates the hotspot helper’s confidence in its ability to handle the network.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum NEHotspotHelperConfidence
```

## Topics

### Confidence Levels
- [NEHotspotHelperConfidence.high](nehotspothelperconfidence/high.md)
  The helper has high confidence in being able to handle the network.
- [NEHotspotHelperConfidence.low](nehotspothelperconfidence/low.md)
  The helper has some confidence in being able to handle the network.
- [NEHotspotHelperConfidence.none](nehotspothelperconfidence/none.md)
  The helper is unable to handle the network.
### Initializers
- [init?(rawValue: Int)](nehotspothelperconfidence/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func setConfidence(NEHotspotHelperConfidence)](nehotspotnetwork/setconfidence(_:).md)
  Indicate the level of confidence in being able to handle the network.
- [func setPassword(String)](nehotspotnetwork/setpassword(_:).md)
  Provide the password for a protected network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence)*