# getPendingDatasetRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command GetPendingDatasetRequest

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
func getPendingDatasetRequest(with params: MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams?, completion: @escaping @Sendable (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)
```

```swift
func pendingDatasetRequest(with params: MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams?) async throws -> MTRThreadBorderRouterManagementClusterDatasetResponseParams
```

```objc
- (void) getPendingDatasetRequestWithParams:(MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams *) params completion:(void (^)(MTRThreadBorderRouterManagementClusterDatasetResponseParams *data, NSError *error)) completion;
```

#### Discussion

This command SHALL be used to request the pending dataset of the Thread network to which the border router is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement/getpendingdatasetrequest(with:completion:))*