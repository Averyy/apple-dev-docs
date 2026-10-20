# delegate

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

The delegate object that handles advertising-related events.

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
weak var delegate: (any MCNearbyServiceAdvertiserDelegate)? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, weak, nullable) id<MCNearbyServiceAdvertiserDelegate> delegate;
```

*macOS*

```objc
@property (atomic, weak, nullable) id<MCNearbyServiceAdvertiserDelegate> delegate;
```

## See Also

### Configuring and Initialization
- [init(peer: MCPeerID, discoveryInfo: [String : String]?, serviceType: String)](./init%28peer,discoveryinfo,servicetype%29.md)
  Initializes an advertiser object.
- [var discoveryInfo: [String : String]?](./discoveryinfo.md)
  The `info` dictionary passed when this object was initialized.
- [var myPeerID: MCPeerID](./mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](./servicetype.md)
  The service type that your app is advertising


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/delegate)*