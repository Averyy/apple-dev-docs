# delegate

**Framework**: Multipeer Connectivity  
**Kind**: property

The delegate object that handles advertising-related events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any MCNearbyServiceAdvertiserDelegate)? { get set }
```

## See Also

- [init(peer: MCPeerID, discoveryInfo: [String : String]?, serviceType: String)](mcnearbyserviceadvertiser/init(peer:discoveryinfo:servicetype:).md)
  Initializes an advertiser object.
- [var discoveryInfo: [String : String]?](mcnearbyserviceadvertiser/discoveryinfo.md)
  The `info` dictionary passed when this object was initialized.
- [var myPeerID: MCPeerID](mcnearbyserviceadvertiser/mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](mcnearbyserviceadvertiser/servicetype.md)
  The service type that your app is advertising


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/delegate)*