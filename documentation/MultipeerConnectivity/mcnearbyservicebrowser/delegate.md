# delegate

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

The delegate object that handles browser-related events.

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
weak var delegate: (any MCNearbyServiceBrowserDelegate)? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, weak, nullable) id<MCNearbyServiceBrowserDelegate> delegate;
```

*macOS*

```objc
@property (atomic, weak, nullable) id<MCNearbyServiceBrowserDelegate> delegate;
```

## See Also

### Initializing the Browser
- [init(peer: MCPeerID, serviceType: String)](./init%28peer,servicetype%29.md)
  Initializes the nearby service browser object.
- [var myPeerID: MCPeerID](./mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](./servicetype.md)
  The service type to browse for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/delegate)*