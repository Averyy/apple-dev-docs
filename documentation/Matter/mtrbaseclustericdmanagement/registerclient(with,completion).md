# registerClient(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command RegisterClient

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
func registerClient(with params: MTRICDManagementClusterRegisterClientParams, completion: @escaping @Sendable (MTRICDManagementClusterRegisterClientResponseParams?, (any Error)?) -> Void)
```

```swift
func registerClient(with params: MTRICDManagementClusterRegisterClientParams) async throws -> MTRICDManagementClusterRegisterClientResponseParams
```

```objc
- (void) registerClientWithParams:(MTRICDManagementClusterRegisterClientParams *) params completion:(void (^)(MTRICDManagementClusterRegisterClientResponseParams *data, NSError *error)) completion;
```

#### Discussion

This command allows a client to register itself with the ICD to be notified when the device is available for communication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustericdmanagement/registerclient(with:completion:))*