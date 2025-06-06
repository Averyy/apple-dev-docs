# discoveryInfo

**Framework**: Multipeer Connectivity  
**Kind**: property

The `info` dictionary passed when this object was initialized.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var discoveryInfo: [String : String]? { get }
```

#### Discussion

This value is set when you initialize the object, and cannot be changed later.

## See Also

- [init(peer: MCPeerID, discoveryInfo: [String : String]?, serviceType: String)](mcnearbyserviceadvertiser/init(peer:discoveryinfo:servicetype:).md)
  Initializes an advertiser object.
- [var delegate: (any MCNearbyServiceAdvertiserDelegate)?](mcnearbyserviceadvertiser/delegate.md)
  The delegate object that handles advertising-related events.
- [var myPeerID: MCPeerID](mcnearbyserviceadvertiser/mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](mcnearbyserviceadvertiser/servicetype.md)
  The service type that your app is advertising


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/discoveryinfo)*