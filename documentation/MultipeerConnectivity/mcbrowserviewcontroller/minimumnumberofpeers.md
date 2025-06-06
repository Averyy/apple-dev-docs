# minimumNumberOfPeers

**Framework**: Multipeer Connectivity  
**Kind**: property

The minimum number of peers that need to be in a session, including the local peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumNumberOfPeers: Int { get set }
```

#### Discussion

The smallest allowable value (and the default) is 2.

## See Also

- [var maximumNumberOfPeers: Int](mcbrowserviewcontroller/maximumnumberofpeers.md)
  The maximum number of peers allowed in a session, including the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/minimumnumberofpeers)*