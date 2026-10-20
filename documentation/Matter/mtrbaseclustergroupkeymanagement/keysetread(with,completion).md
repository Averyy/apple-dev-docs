# keySetRead(with:completion:)

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
func keySetRead(with params: MTRGroupKeyManagementClusterKeySetReadParams, completion: @escaping @Sendable (MTRGroupKeyManagementClusterKeySetReadResponseParams?, (any Error)?) -> Void)
```

```swift
func keySetRead(with params: MTRGroupKeyManagementClusterKeySetReadParams) async throws -> MTRGroupKeyManagementClusterKeySetReadResponseParams
```

```objc
- (void) keySetReadWithParams:(MTRGroupKeyManagementClusterKeySetReadParams *) params completion:(void (^)(MTRGroupKeyManagementClusterKeySetReadResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroupkeymanagement/keysetread(with:completion:))*