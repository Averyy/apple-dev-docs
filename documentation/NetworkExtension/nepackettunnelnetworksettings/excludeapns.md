# excludeAPNs

**Framework**: Network Extension  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var excludeAPNs: Bool { get set }
```

#### Discussion

If includeAllNetworks is set to YES and this property is set to YES, then network traffic for the Apple Push Notification service (APNs) is excluded from the tunnel. The default value of this property is YES. If either the includeAllNetworks property in NEVPNProtocol class is set, then the excludeAPNs property in NEVPNProtocol class takes precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/excludeapns)*