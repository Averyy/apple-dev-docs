# localEndpoint

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An [`NWEndpoint`](../nwendpoint.md) object containing information about the local endpoint of the flow.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
var localEndpoint: NWEndpoint? { get }
```

```objc
@property (readonly, nullable) NWEndpoint * localEndpoint;
```

## Discussion

This property may be nil if the corresponding UDP socket was not bound to a port by the application and the App Proxy Provider did not set a local endpoint in [`open(withLocalEndpoint:completionHandler:)`](../neappproxyflow/open%28withlocalendpoint,completionhandler%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyudpflow/localendpoint)*