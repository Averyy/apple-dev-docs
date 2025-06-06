# init(peer:discoveryInfo:serviceType:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Initializes an advertiser object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(peer myPeerID: MCPeerID, discoveryInfo info: [String : String]?, serviceType: String)
```

#### Return Value

Returns an initialized instance, or `nil` if an error occurred.

#### Discussion

This method throws an exception if a valid `peerID` object is not provided or if the value of `serviceType` is not a legal Bonjour service type.

## Parameters

- `myPeerID`: Your app’s local peer ID.
- `info`: If the data you need to provide is too large to fit within these constraints, you should create a custom discovery class using Bonjour for discovery and your choice of networking protocols for exchanging the information.
- `serviceType`: For more details, read  .

## See Also

- [var delegate: (any MCNearbyServiceAdvertiserDelegate)?](mcnearbyserviceadvertiser/delegate.md)
  The delegate object that handles advertising-related events.
- [var discoveryInfo: [String : String]?](mcnearbyserviceadvertiser/discoveryinfo.md)
  The `info` dictionary passed when this object was initialized.
- [var myPeerID: MCPeerID](mcnearbyserviceadvertiser/mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](mcnearbyserviceadvertiser/servicetype.md)
  The service type that your app is advertising


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/init(peer:discoveryinfo:servicetype:))*