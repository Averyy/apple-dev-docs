# networkPassphraseRequest(with:completion:)

**Framework**: Matter  
**Kind**: method

Command NetworkPassphraseRequest

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func networkPassphraseRequest(with params: MTRWiFiNetworkManagementClusterNetworkPassphraseRequestParams?) async throws -> MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams
```

#### Discussion

This command is used to request the current WPA-Personal passphrase or PSK associated with the Wi-Fi network provided by this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterwifinetworkmanagement/networkpassphraserequest(with:completion:))*