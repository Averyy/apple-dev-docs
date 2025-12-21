# commissioning(_:completedDeviceAttestation:error:completion:)

**Framework**: Matter  
**Kind**: method  
**Required**: Yes

Notification that device attestation has completed.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
func commissioning(_ commissioning: MTRCommissioningOperation, completedDeviceAttestation attestationDeviceInfo: MTRDeviceAttestationDeviceInfo, error: (any Error)?) async
```

#### Discussion

Commissioning will pause, regardless of whether attestation succeeded or failed, until the completion is invoked (indicating that commissioning should proceed, even if attestation failed), or commissioning is stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate/commissioning(_:completeddeviceattestation:error:completion:))*