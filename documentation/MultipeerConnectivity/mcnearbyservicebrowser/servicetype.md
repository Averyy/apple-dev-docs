# serviceType

**Framework**: Multipeer Connectivity  
**Kind**: property

The service type to browse for.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var serviceType: String { get }
```

#### Discussion

This value is set when you initialize the object, and cannot be changed later.

## See Also

- [init(peer: MCPeerID, serviceType: String)](mcnearbyservicebrowser/init(peer:servicetype:).md)
  Initializes the nearby service browser object.
- [var delegate: (any MCNearbyServiceBrowserDelegate)?](mcnearbyservicebrowser/delegate.md)
  The delegate object that handles browser-related events.
- [var myPeerID: MCPeerID](mcnearbyservicebrowser/mypeerid.md)
  The local peer ID for this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/servicetype)*