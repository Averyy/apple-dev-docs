# maximumNumberOfPeers

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

The maximum number of peers allowed in a session, including the local peer.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
var maximumNumberOfPeers: Int { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, assign) NSUInteger maximumNumberOfPeers;
```

*macOS*

```objc
@property (atomic, assign) NSUInteger maximumNumberOfPeers;
```

## Discussion

The largest allowable value (and the default) is 8.

## See Also

### Getting and Setting the Maximum and Minimum Number of Peers
- [var minimumNumberOfPeers: Int](./minimumnumberofpeers.md)
  The minimum number of peers that need to be in a session, including the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/maximumnumberofpeers)*