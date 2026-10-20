# changeToMode(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ChangeToMode

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
func changeToMode(with params: MTRDeviceEnergyManagementModeClusterChangeToModeParams, completion: @escaping @Sendable (MTRDeviceEnergyManagementModeClusterChangeToModeResponseParams?, (any Error)?) -> Void)
```

```swift
func changeToMode(with params: MTRDeviceEnergyManagementModeClusterChangeToModeParams) async throws -> MTRDeviceEnergyManagementModeClusterChangeToModeResponseParams
```

```objc
- (void) changeToModeWithParams:(MTRDeviceEnergyManagementModeClusterChangeToModeParams *) params completion:(void (^)(MTRDeviceEnergyManagementModeClusterChangeToModeResponseParams *data, NSError *error)) completion;
```

#### Discussion

This command is used to change device modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagementmode/changetomode(with:completion:))*