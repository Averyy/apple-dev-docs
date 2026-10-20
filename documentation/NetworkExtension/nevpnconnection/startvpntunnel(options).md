# startVPNTunnel(options:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Start the process of connecting the VPN.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func startVPNTunnel(options: [String : NSObject]? = nil) throws
```

```objc
- (BOOL) startVPNTunnelWithOptions:(NSDictionary<NSString *,NSObject *> *) options andReturnError:(NSError **) error;
```

#### Discussion

This method returns immediately after starting the process of connecting the VPN. In order to be notified when the VPN is fully connected, register to observe the [`NEVPNStatusDidChangeNotification`](../nevpnstatusdidchangenotification.md) notification on the [`NEVPNConnection`](../nevpnconnection.md) object, and examine the status property when the notification is received.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `options`: An `NSDictionary` that will be passed to the tunnel provider during the process of starting the tunnel. See Constants, below.

## See Also

### Controlling the VPN connection
- [func startVPNTunnel() throws](./startvpntunnel%28%29.md)
  Start the process of connecting the VPN.
- [let NEVPNConnectionStartOptionUsername: String](../nevpnconnectionstartoptionusername.md)
- [let NEVPNConnectionStartOptionPassword: String](../nevpnconnectionstartoptionpassword.md)
- [func stopVPNTunnel()](./stopvpntunnel%28%29.md)
  Start the process of disconnecting the VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection/startvpntunnel(options:))*