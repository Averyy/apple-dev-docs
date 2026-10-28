# getOperationalDataset(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command GetOperationalDataset

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
func getOperationalDataset(with params: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams, completion: @escaping @Sendable (MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams?, (any Error)?) -> Void)
```

```swift
func operationalDataset(with params: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams) async throws -> MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams
```

```objc
- (void) getOperationalDatasetWithParams:(MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams *) params completion:(void (^)(MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams *data, NSError *error)) completion;
```

## Discussion

Retrieves the Thread Operational Dataset with the given Extended PAN ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadnetworkdirectory/getoperationaldataset(with:completion:))*