# peerDiscoveryToken

**Framework**: Nearby Interaction  
**Kind**: property

A value that uniquely identifies the other peer in the interaction session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
@NSCopying
var peerDiscoveryToken: NIDiscoveryToken { get }
```

#### Discussion

NI sets this property to the value of the peer discovery token you pass to the [`init(peerToken:)`](ninearbypeerconfiguration/init(peertoken:).md) initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbypeerconfiguration/peerdiscoverytoken)*