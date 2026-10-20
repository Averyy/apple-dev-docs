# retrieveLogsRequest(with:expectedValues:expectedValueInterval:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use retrieveLogsRequestWithParams:expectedValues:expectedValueInterval:completion:

## Declaration

```swift
func retrieveLogsRequest(with params: MTRDiagnosticLogsClusterRetrieveLogsRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completionHandler: @escaping @Sendable (MTRDiagnosticLogsClusterRetrieveLogsResponseParams?, (any Error)?) -> Void)
```

```swift
func retrieveLogsRequest(with params: MTRDiagnosticLogsClusterRetrieveLogsRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRDiagnosticLogsClusterRetrieveLogsResponseParams
```

```objc
- (void) retrieveLogsRequestWithParams:(MTRDiagnosticLogsClusterRetrieveLogsRequestParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completionHandler:(void (^)(MTRDiagnosticLogsClusterRetrieveLogsResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdiagnosticlogs/retrievelogsrequest(with:expectedvalues:expectedvalueinterval:completionhandler:))*