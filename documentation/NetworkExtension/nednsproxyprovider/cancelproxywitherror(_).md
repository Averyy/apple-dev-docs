# cancelProxyWithError(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Cancels the DNS proxy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func cancelProxyWithError(_ error: (any Error)?)
```

```objc
- (void) cancelProxyWithError:(NSError *) error;
```

#### Discussion

Call this method from within the proxy provider when you need to stop the proxy due to a network error that renders the proxy no longer viable.

> ❗ **Important**:  Subclasses should not override this method.

## Parameters

- `error`: An error instance containing details about the problem that the proxy provider implementation encountered.

## See Also

### Managing the DNS proxy life cycle
- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](./startproxy%28options,completionhandler%29.md)
  Starts the DNS proxy.
- [func stopProxy(with: NEProviderStopReason, completionHandler: () -> Void)](./stopproxy%28with,completionhandler%29.md)
  Stops the DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyprovider/cancelproxywitherror(_:))*