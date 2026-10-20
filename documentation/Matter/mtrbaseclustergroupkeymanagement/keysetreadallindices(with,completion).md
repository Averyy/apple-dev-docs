# keySetReadAllIndices(with:completion:)

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
func keySetReadAllIndices(with params: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?, completion: @escaping @Sendable (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)
```

```swift
func keySetReadAllIndices(with params: MTRGroupKeyManagementClusterKeySetReadAllIndicesParams?) async throws -> MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams
```

```objc
- (void) keySetReadAllIndicesWithParams:(MTRGroupKeyManagementClusterKeySetReadAllIndicesParams *) params completion:(void (^)(MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroupkeymanagement/keysetreadallindices(with:completion:))*