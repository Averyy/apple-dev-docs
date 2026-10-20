# retrieveLogsRequest(with:expectedValues:expectedValueInterval:completion:)

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
func retrieveLogsRequest(with params: MTRDiagnosticLogsClusterRetrieveLogsRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRDiagnosticLogsClusterRetrieveLogsResponseParams?, (any Error)?) -> Void)
```

```swift
func retrieveLogsRequest(with params: MTRDiagnosticLogsClusterRetrieveLogsRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDiagnosticLogsClusterRetrieveLogsResponseParams
```

```objc
- (void) retrieveLogsRequestWithParams:(MTRDiagnosticLogsClusterRetrieveLogsRequestParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRDiagnosticLogsClusterRetrieveLogsResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdiagnosticlogs/retrievelogsrequest(with:expectedvalues:expectedvalueinterval:completion:))*