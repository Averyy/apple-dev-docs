# getActiveDatasetRequest(with:completion:)

**Framework**: Matter  
**Kind**: method

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
func activeDatasetRequest(with params: MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams?) async throws -> MTRThreadBorderRouterManagementClusterDatasetResponseParams
```

#### Discussion

Command to request the active operational dataset of the Thread network to which the border router is connected. This command must be sent over a valid CASE session


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement/getactivedatasetrequest(with:completion:))*