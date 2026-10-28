# startTunnel(options:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Start the process of connecting the tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func startTunnel(options: [String : Any]? = nil) throws
```

```objc
- (BOOL) startTunnelWithOptions:(NSDictionary<NSString *,id> *) options andReturnError:(NSError **) error;
```

## Discussion

This method returns immediately after starting the process of connecting the tunnel. In order to be notified when the tunnel is fully connected, register to observe the [`NEVPNStatusDidChangeNotification`](../nevpnstatusdidchangenotification.md) notification on the `NETunnelProviderSession` object and examine its status property when the notification is received.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `options`: A dictionary containing options to be passed to the Tunnel Provider extension.

## See Also

### Controlling the tunnel connection
- [func stopTunnel()](./stoptunnel%28%29.md)
  Start the process of disconnecting the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/starttunnel(options:))*