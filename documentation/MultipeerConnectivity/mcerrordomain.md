# MCErrorDomain

**Framework**: Multipeer Connectivity  
**Kind**: var  
**Role**: Global Variable

The `NSError` domain constant. If the `domain` value for an `NSError` object is equal to `MCErrorDomain`, then the error was produced by the Multipeer Connectivity framework itself, as opposed to a lower-level framework on which it depends.

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
let MCErrorDomain: String
```

```c
extern NSString * const MCErrorDomain;
```

## See Also

### Constants
- [let kMCSessionMaximumNumberOfPeers: Int](./kmcsessionmaximumnumberofpeers.md)
  The maximum number of peers that a session can support, including the local peer.
- [let kMCSessionMinimumNumberOfPeers: Int](./kmcsessionminimumnumberofpeers.md)
  The minimum number of peers that a session can support, including the local peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcerrordomain)*