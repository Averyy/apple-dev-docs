# setPendingDatasetRequestWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetPendingDatasetRequest

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
func setPendingDatasetRequestWith(_ params: MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setPendingDatasetRequestWith(_ params: MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams) async throws
```

```objc
- (void) setPendingDatasetRequestWithParams:(MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command SHALL be used to set or update the pending Dataset of the Thread network to which the Border Router is connected, if the Border Router supports PANChange Feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement/setpendingdatasetrequestwith(_:completion:))*