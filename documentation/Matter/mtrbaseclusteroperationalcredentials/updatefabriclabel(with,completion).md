# updateFabricLabel(with:completion:)

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
func updateFabricLabel(with params: MTROperationalCredentialsClusterUpdateFabricLabelParams, completion: @escaping @Sendable (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)
```

```swift
func updateFabricLabel(with params: MTROperationalCredentialsClusterUpdateFabricLabelParams) async throws -> MTROperationalCredentialsClusterNOCResponseParams
```

```objc
- (void) updateFabricLabelWithParams:(MTROperationalCredentialsClusterUpdateFabricLabelParams *) params completion:(void (^)(MTROperationalCredentialsClusterNOCResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalcredentials/updatefabriclabel(with:completion:))*