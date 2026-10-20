# stopProxy(with:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Stop the network proxy.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func stopProxy(with reason: NEProviderStopReason, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func stopProxy(with reason: NEProviderStopReason) async
```

```objc
- (void) stopProxyWithReason:(NEProviderStopReason) reason completionHandler:(void (^)()) completionHandler;
```

#### Discussion

This method is called by the system to stop the network proxy.

`NEAppProxyProvider` subclasses must override this method.

Do not use this method to stop the proxy from the App Proxy Provider. Use `cancelProxyWithError:` instead.

## Parameters

- `reason`: A `NEProviderStopReason` code indicating why the proxy is being stopped. For a list of possible codes, see [`NEProvider`](../neprovider.md).
- `completionHandler`: A block that must be executed when the proxy is fully stopped.

## See Also

### Managing the app proxy life cycle
- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](./startproxy%28options,completionhandler%29.md)
  Start the network proxy.
- [func cancelProxyWithError((any Error)?)](./cancelproxywitherror%28_%29.md)
  Stop the network proxy from the App Proxy Provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovider/stopproxy(with:completionhandler:))*