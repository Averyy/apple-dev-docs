# myPeerID

**Framework**: Multipeer Connectivity  
**Kind**: property

The local peer ID for this instance.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var myPeerID: MCPeerID { get }
```

#### Discussion

This value is set when you initialize the object, and cannot be changed later.

## See Also

- [init(peer: MCPeerID, serviceType: String)](mcnearbyservicebrowser/init(peer:servicetype:).md)
  Initializes the nearby service browser object.
- [var delegate: (any MCNearbyServiceBrowserDelegate)?](mcnearbyservicebrowser/delegate.md)
  The delegate object that handles browser-related events.
- [var serviceType: String](mcnearbyservicebrowser/servicetype.md)
  The service type to browse for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/mypeerid)*