# registerClient(with:completion:)

**Framework**: Matter  
**Kind**: method

Command RegisterClient

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
func registerClient(with params: MTRICDManagementClusterRegisterClientParams) async throws -> MTRICDManagementClusterRegisterClientResponseParams
```

#### Discussion

This command allows a client to register itself with the ICD to be notified when the device is available for communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustericdmanagement/registerclient(with:completion:))*