# unregisterClient(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command UnregisterClient

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
func unregisterClient(with params: MTRICDManagementClusterUnregisterClientParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func unregisterClient(with params: MTRICDManagementClusterUnregisterClientParams) async throws
```

```objc
- (void) unregisterClientWithParams:(MTRICDManagementClusterUnregisterClientParams *) params completion:(MTRStatusCompletion) completion;
```

#### Discussion

This command allows a client to unregister itself with the ICD.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustericdmanagement/unregisterclient(with:completion:))*