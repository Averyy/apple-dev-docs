# excludeDeviceCommunication

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

## Declaration

```objc
@property BOOL excludeDeviceCommunication;
```

#### Discussion

If includeAllNetworks is set to YES and this property is set to YES, then network traffic used for communicating with devices connected via USB or Wi-Fi is excluded from the tunnel. For example, Xcode uses a network tunnel to communicate with connected development devices like iPhone, iPad and TV. The default value of this property is YES. If either the includeAllNetworks property in NEVPNProtocol class is set, then the excludeDeviceCommunication property in NEVPNProtocol class takes precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelnetworksettings/excludedevicecommunication)*