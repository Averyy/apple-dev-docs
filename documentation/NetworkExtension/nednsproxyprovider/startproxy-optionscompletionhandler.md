# startProxy(options:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Starts the DNS proxy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func startProxy(options: [String : Any]? = nil) async throws
```

#### Discussion

Subclasses of [`NEDNSProxyProvider`](nednsproxyprovider.md) must override this method to perform any necessary steps to ready the proxy for handling flows of network data.

The framework calls this method when a new proxy instance is created. You indicate that setup is complete by calling the completion handler with a `nil` error parameter, or that setup failed by calling the completion handler with an error instance. You define the error domain and code.

## Parameters

- `options`: A dictionary that you define as part of a device configuration profile. You can also modify the contents of this dictionary from your app using the shared instance of  . The dictionary appears as the   component of the manager’s   property.
- `completionHandler`: A block that you must execute when the proxy is fully established, or when the proxy cannot be started due to an error. If the proxy is successfully established, the error parameter should be set to  . Otherwise, the error parameter passed to this block indicates the reason for failure.

## See Also

- [func stopProxy(with: NEProviderStopReason, completionHandler: () -> Void)](nednsproxyprovider/stopproxy(with:completionhandler:).md)
  Stops the DNS proxy.
- [func cancelProxyWithError((any Error)?)](nednsproxyprovider/cancelproxywitherror(_:).md)
  Cancels the DNS proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxyprovider/startproxy(options:completionhandler:))*