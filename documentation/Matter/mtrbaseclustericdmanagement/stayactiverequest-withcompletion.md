# stayActiveRequest(with:completion:)

**Framework**: Matter  
**Kind**: method

Command StayActiveRequest

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
func stayActiveRequest(with params: MTRICDManagementClusterStayActiveRequestParams) async throws -> MTRICDManagementClusterStayActiveResponseParams
```

#### Discussion

This command allows a client to request that the server stays in active mode for at least a given time duration (in milliseconds) from when this command is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustericdmanagement/stayactiverequest(with:completion:))*