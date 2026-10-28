# cancelProxyWithError(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancelProxyWithError:(NSError *) error;
```

## Discussion

The App Proxy Provider should call this method when an unrecoverable error occurs that makes the proxy no longer viable.

## Parameters

- `error`: An [`NSError`](../../Foundation/nserror.md) object containing the error that caused the proxy to be stopped. The domain and code of this `NSError` object is defined by the caller.

## See Also

### Managing the app proxy life cycle
- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](./startproxy%28options,completionhandler%29.md)
  Start the network proxy.
- [func stopProxy(with: NEProviderStopReason, completionHandler: () -> Void)](./stopproxy%28with,completionhandler%29.md)
  Stop the network proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovider/cancelproxywitherror(_:))*