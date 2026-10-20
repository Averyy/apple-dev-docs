# keySetRemove(with:completion:)

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
func keySetRemove(with params: MTRGroupKeyManagementClusterKeySetRemoveParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func keySetRemove(with params: MTRGroupKeyManagementClusterKeySetRemoveParams) async throws
```

```objc
- (void) keySetRemoveWithParams:(MTRGroupKeyManagementClusterKeySetRemoveParams *) params completion:(MTRStatusCompletion) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustergroupkeymanagement/keysetremove(with:completion:))*