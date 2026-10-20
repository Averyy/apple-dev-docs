# failedToJoinNetwork

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

The accessory failed to join the network.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var failedToJoinNetwork: HMError.Code { get }
```

## See Also

### Detecting network errors
- [static var enterpriseNetworkNotSupported: HMError.Code](./enterprisenetworknotsupported.md)
  An enterprise network doesn’t support this accessory.
- [static var incompatibleNetwork: HMError.Code](./incompatiblenetwork.md)
  An error indicating an incompatible network.
- [static var networkUnavailable: HMError.Code](./networkunavailable.md)
  An error indicating the network is unavailable.
- [static var wiFiCredentialGenerationFailed: HMError.Code](./wificredentialgenerationfailed.md)
  WiFi credential generation failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/failedtojoinnetwork)*