# excludeAPNs

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

## Declaration

```objc
@property BOOL excludeAPNs;
```

## Discussion

If includeAllNetworks is set to YES and this property is set to YES, then network traffic for the Apple Push Notification service (APNs) is excluded from the tunnel. The default value of this property is YES. If either the includeAllNetworks property in NEVPNProtocol class is set, then the excludeAPNs property in NEVPNProtocol class takes precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/excludeapns)*