# NEHotspotHelperConfidence

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NEHotspotHelperConfidence : NSInteger;
```

## Topics

### Confidence Levels
- [NEHotspotHelperConfidence.high](./nehotspothelperconfidence/high.md)
  The helper has high confidence in being able to handle the network.
- [NEHotspotHelperConfidence.low](./nehotspothelperconfidence/low.md)
  The helper has some confidence in being able to handle the network.
- [NEHotspotHelperConfidence.none](./nehotspothelperconfidence/none.md)
  The helper is unable to handle the network.
### Initializers
- [init?(rawValue: Int)](./nehotspothelperconfidence/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Network annotation
- [func setConfidence(NEHotspotHelperConfidence)](./nehotspotnetwork/setconfidence%28_%29.md)
  Indicate the level of confidence in being able to handle the network.
- [func setPassword(String)](./nehotspotnetwork/setpassword%28_%29.md)
  Provide the password for a protected network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelperconfidence)*