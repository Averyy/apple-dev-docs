# removeFabric(with:completion:)

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
func removeFabric(with params: MTROperationalCredentialsClusterRemoveFabricParams, completion: @escaping @Sendable (MTROperationalCredentialsClusterNOCResponseParams?, (any Error)?) -> Void)
```

```swift
func removeFabric(with params: MTROperationalCredentialsClusterRemoveFabricParams) async throws -> MTROperationalCredentialsClusterNOCResponseParams
```

```objc
- (void) removeFabricWithParams:(MTROperationalCredentialsClusterRemoveFabricParams *) params completion:(void (^)(MTROperationalCredentialsClusterNOCResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusteroperationalcredentials/removefabric(with:completion:))*