# reorderNetwork(with:completion:)

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
func reorderNetwork(with params: MTRNetworkCommissioningClusterReorderNetworkParams, completion: @escaping @Sendable (MTRNetworkCommissioningClusterNetworkConfigResponseParams?, (any Error)?) -> Void)
```

```swift
func reorderNetwork(with params: MTRNetworkCommissioningClusterReorderNetworkParams) async throws -> MTRNetworkCommissioningClusterNetworkConfigResponseParams
```

```objc
- (void) reorderNetworkWithParams:(MTRNetworkCommissioningClusterReorderNetworkParams *) params completion:(void (^)(MTRNetworkCommissioningClusterNetworkConfigResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusternetworkcommissioning/reordernetwork(with:completion:))*