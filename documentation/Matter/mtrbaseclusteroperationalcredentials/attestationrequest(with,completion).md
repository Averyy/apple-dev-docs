# attestationRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func attestationRequest(with params: MTROperationalCredentialsClusterAttestationRequestParams, completion: @escaping @Sendable (MTROperationalCredentialsClusterAttestationResponseParams?, (any Error)?) -> Void)
```

```swift
func attestationRequest(with params: MTROperationalCredentialsClusterAttestationRequestParams) async throws -> MTROperationalCredentialsClusterAttestationResponseParams
```

```objc
- (void) attestationRequestWithParams:(MTROperationalCredentialsClusterAttestationRequestParams *) params completion:(void (^)(MTROperationalCredentialsClusterAttestationResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalcredentials/attestationrequest(with:completion:))*