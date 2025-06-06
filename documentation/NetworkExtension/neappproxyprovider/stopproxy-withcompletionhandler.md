# stopProxy(with:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Stop the network proxy.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func stopProxy(with reason: NEProviderStopReason) async
```

#### Discussion

This method is called by the system to stop the network proxy.

`NEAppProxyProvider` subclasses must override this method.

Do not use this method to stop the proxy from the App Proxy Provider. Use `cancelProxyWithError:` instead.

## Parameters

- `reason`: A   code indicating why the proxy is being stopped. For a list of possible codes, see  .
- `completionHandler`: A block that must be executed when the proxy is fully stopped.

## See Also

- [func startProxy(options: [String : Any]?, completionHandler: ((any Error)?) -> Void)](neappproxyprovider/startproxy(options:completionhandler:).md)
  Start the network proxy.
- [func cancelProxyWithError((any Error)?)](neappproxyprovider/cancelproxywitherror(_:).md)
  Stop the network proxy from the App Proxy Provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovider/stopproxy(with:completionhandler:))*