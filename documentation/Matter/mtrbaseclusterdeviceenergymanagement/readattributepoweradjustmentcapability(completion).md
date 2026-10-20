# readAttributePowerAdjustmentCapability(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func readAttributePowerAdjustmentCapability(completion: @escaping @Sendable (MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct?, (any Error)?) -> Void)
```

```swift
func readAttributePowerAdjustmentCapability() async throws -> MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct
```

```objc
- (void) readAttributePowerAdjustmentCapabilityWithCompletion:(void (^)(MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement/readattributepoweradjustmentcapability(completion:))*