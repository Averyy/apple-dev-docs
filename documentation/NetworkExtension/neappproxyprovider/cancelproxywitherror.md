# cancelProxyWithError(_:)

**Framework**: Network Extension  
**Kind**: method

Stop the network proxy from the App Proxy Provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func cancelProxyWithError(_ error: (any Error)?)
```

#### Discussion

The App Proxy Provider should call this method when an unrecoverable error occurs that makes the proxy no longer viable.

## Parameters

- `error`: An   object containing the error that caused the proxy to be stopped. The domain and code of this   object is defined by the caller.

## See Also

- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](neappproxyprovider/startproxy(options:completionhandler:).md)
  Start the network proxy.
- [func stopProxy(with: NEProviderStopReason, completionHandler: () -> Void)](neappproxyprovider/stopproxy(with:completionhandler:).md)
  Stop the network proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovider/cancelproxywitherror(_:))*