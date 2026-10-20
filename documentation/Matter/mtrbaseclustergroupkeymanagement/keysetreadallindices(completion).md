# keySetReadAllIndices(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func keySetReadAllIndices(completion: @escaping @Sendable (MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams?, (any Error)?) -> Void)
```

```swift
func keySetReadAllIndices() async throws -> MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams
```

```objc
- (void) keySetReadAllIndicesWithCompletion:(void (^)(MTRGroupKeyManagementClusterKeySetReadAllIndicesResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroupkeymanagement/keysetreadallindices(completion:))*