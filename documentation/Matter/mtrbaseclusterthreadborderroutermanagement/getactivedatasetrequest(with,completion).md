# getActiveDatasetRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command GetActiveDatasetRequest

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
func getActiveDatasetRequest(with params: MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams?, completion: @escaping @Sendable (MTRThreadBorderRouterManagementClusterDatasetResponseParams?, (any Error)?) -> Void)
```

```swift
func activeDatasetRequest(with params: MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams?) async throws -> MTRThreadBorderRouterManagementClusterDatasetResponseParams
```

```objc
- (void) getActiveDatasetRequestWithParams:(MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams *) params completion:(void (^)(MTRThreadBorderRouterManagementClusterDatasetResponseParams *data, NSError *error)) completion;
```

## Discussion

This command SHALL be used to request the active operational dataset of the Thread network to which the border router is connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement/getactivedatasetrequest(with:completion:))*