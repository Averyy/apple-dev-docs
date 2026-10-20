# testNullableOptionalRequest(with:completionHandler:)

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

> **Deprecated**: Please use testNullableOptionalRequestWithParams:completion:

## Declaration

```swift
func testNullableOptionalRequest(with params: MTRTestClusterClusterTestNullableOptionalRequestParams?, completionHandler: @escaping @Sendable (MTRTestClusterClusterTestNullableOptionalResponseParams?, (any Error)?) -> Void)
```

```swift
func testNullableOptionalRequest(with params: MTRTestClusterClusterTestNullableOptionalRequestParams?) async throws -> MTRTestClusterClusterTestNullableOptionalResponseParams
```

```objc
- (void) testNullableOptionalRequestWithParams:(MTRTestClusterClusterTestNullableOptionalRequestParams *) params completionHandler:(void (^)(MTRTestClusterClusterTestNullableOptionalResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertestcluster/testnullableoptionalrequest(with:completionhandler:))*