# keepActive(with:completion:)

**Framework**: Matter  
**Kind**: method

Command KeepActive

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
func keepActive(with params: MTRBridgedDeviceBasicInformationClusterKeepActiveParams) async throws
```

#### Discussion

Upon receipt, the server SHALL attempt to keep the bridged device active for the duration specified by the command, when the device is next active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbridgeddevicebasicinformation/keepactive(with:completion:))*