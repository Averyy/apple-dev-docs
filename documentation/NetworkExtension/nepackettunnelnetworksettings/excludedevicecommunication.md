# excludeDeviceCommunication

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
var excludeDeviceCommunication: Bool { get set }
```

#### Discussion

If includeAllNetworks is set to YES and this property is set to YES, then network traffic used for communicating with devices connected via USB or Wi-Fi is excluded from the tunnel. For example, Xcode uses a network tunnel to communicate with connected development devices like iPhone, iPad and TV. The default value of this property is YES. If either the includeAllNetworks property in NEVPNProtocol class is set, then the excludeDeviceCommunication property in NEVPNProtocol class takes precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/excludedevicecommunication)*