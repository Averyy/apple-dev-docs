# testSimpleArgumentRequest(with:expectedValues:expectedValueInterval:completionHandler:)

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

> **Deprecated**: Please use testSimpleArgumentRequestWithParams:expectedValues:expectedValueInterval:completion:

## Declaration

```swift
func testSimpleArgumentRequest(with params: MTRTestClusterClusterTestSimpleArgumentRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completionHandler: @escaping @Sendable (MTRTestClusterClusterTestSimpleArgumentResponseParams?, (any Error)?) -> Void)
```

```swift
func testSimpleArgumentRequest(with params: MTRTestClusterClusterTestSimpleArgumentRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRTestClusterClusterTestSimpleArgumentResponseParams
```

```objc
- (void) testSimpleArgumentRequestWithParams:(MTRTestClusterClusterTestSimpleArgumentRequestParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completionHandler:(void (^)(MTRTestClusterClusterTestSimpleArgumentResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustertestcluster/testsimpleargumentrequest(with:expectedvalues:expectedvalueinterval:completionhandler:))*