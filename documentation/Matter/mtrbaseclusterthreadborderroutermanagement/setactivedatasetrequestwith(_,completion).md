# setActiveDatasetRequestWith(_:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command SetActiveDatasetRequest

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
func setActiveDatasetRequestWith(_ params: MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func setActiveDatasetRequestWith(_ params: MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams) async throws
```

```objc
- (void) setActiveDatasetRequestWithParams:(MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command SHALL be used to set the active Dataset of the Thread network to which the Border Router is connected, when there is no active dataset already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement/setactivedatasetrequestwith(_:completion:))*