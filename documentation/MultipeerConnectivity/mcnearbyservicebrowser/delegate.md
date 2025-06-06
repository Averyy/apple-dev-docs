# delegate

**Framework**: Multipeer Connectivity  
**Kind**: property

The delegate object that handles browser-related events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any MCNearbyServiceBrowserDelegate)? { get set }
```

## See Also

- [init(peer: MCPeerID, serviceType: String)](mcnearbyservicebrowser/init(peer:servicetype:).md)
  Initializes the nearby service browser object.
- [var myPeerID: MCPeerID](mcnearbyservicebrowser/mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](mcnearbyservicebrowser/servicetype.md)
  The service type to browse for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/delegate)*