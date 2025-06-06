# init(peer:serviceType:)

**Framework**: Multipeer Connectivity  
**Kind**: init

Initializes the nearby service browser object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(peer myPeerID: MCPeerID, serviceType: String)
```

#### Return Value

Returns an initialized nearby service browser object, or `nil` if an error occurs.

#### Discussion

This method throws an exception if the `session` or `serviceType` parameters do not contain valid objects or the specified Bonjour service type is not valid.

## Parameters

- `myPeerID`: The local peer ID for this instance.
- `serviceType`: For more details, read  .

## See Also

- [var delegate: (any MCNearbyServiceBrowserDelegate)?](mcnearbyservicebrowser/delegate.md)
  The delegate object that handles browser-related events.
- [var myPeerID: MCPeerID](mcnearbyservicebrowser/mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](mcnearbyservicebrowser/servicetype.md)
  The service type to browse for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/init(peer:servicetype:))*