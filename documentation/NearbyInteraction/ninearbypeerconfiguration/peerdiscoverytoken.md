# peerDiscoveryToken

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NIDiscoveryToken * peerDiscoveryToken;
```

#### Discussion

NI sets this property to the value of the peer discovery token you pass to the [`init(peerToken:)`](./init%28peertoken%29.md) initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/ninearbypeerconfiguration/peerdiscoverytoken)*