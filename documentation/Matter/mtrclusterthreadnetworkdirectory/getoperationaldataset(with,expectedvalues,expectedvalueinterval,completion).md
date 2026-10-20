# getOperationalDataset(with:expectedValues:expectedValueInterval:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

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
func getOperationalDataset(with params: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams?, (any Error)?) -> Void)
```

```swift
func operationalDataset(with params: MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams
```

```objc
- (void) getOperationalDatasetWithParams:(MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthreadnetworkdirectory/getoperationaldataset(with:expectedvalues:expectedvalueinterval:completion:))*