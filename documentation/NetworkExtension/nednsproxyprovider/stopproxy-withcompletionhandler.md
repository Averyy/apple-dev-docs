# stopProxy(with:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Stops the DNS proxy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func stopProxy(with reason: NEProviderStopReason) async
```

#### Discussion

Subclasses of [`NEDNSProxyProvider`](nednsproxyprovider.md) must override this method to perform whatever steps are necessary to stop the proxy.

The system calls this method to stop the proxy. You indicate that the proxy is fully stopped by calling the completion handler.

> ❗ **Important**:  Don’t call this method to stop the proxy from within the proxy provider itself. Call [`cancelProxyWithError(_:)`](nednsproxyprovider/cancelproxywitherror(_:).md) instead.

 Don’t call this method to stop the proxy from within the proxy provider itself. Call [`cancelProxyWithError(_:)`](nednsproxyprovider/cancelproxywitherror(_:).md) instead.

## Parameters

- `reason`: A code indicating why the proxy is being stopped.
- `completionHandler`: A block that must be called when the proxy is completely stopped.

## See Also

- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](nednsproxyprovider/startproxy(options:completionhandler:).md)
  Starts the DNS proxy.
- [func cancelProxyWithError((any Error)?)](nednsproxyprovider/cancelproxywitherror(_:).md)
  Cancels the DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyprovider/stopproxy(with:completionhandler:))*