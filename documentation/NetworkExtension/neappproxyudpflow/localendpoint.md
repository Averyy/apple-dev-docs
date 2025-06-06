# localEndpoint

**Framework**: Network Extension  
**Kind**: property

An [`NWEndpoint`](nwendpoint.md) object containing information about the local endpoint of the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var localEndpoint: NWEndpoint? { get }
```

#### Discussion

This property may be nil if the corresponding UDP socket was not bound to a port by the application and the App Proxy Provider did not set a local endpoint in [`open(withLocalEndpoint:completionHandler:)`](neappproxyflow/open(withlocalendpoint:completionhandler:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/localendpoint)*