# testListInt8UArgumentRequest(with:completionHandler:)

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

> **Deprecated**: Please use testListInt8UArgumentRequestWithParams:completion:

## Declaration

```swift
func testListInt8UArgumentRequest(with params: MTRTestClusterClusterTestListInt8UArgumentRequestParams, completionHandler: @escaping @Sendable (MTRTestClusterClusterBooleanResponseParams?, (any Error)?) -> Void)
```

```swift
func testListInt8UArgumentRequest(with params: MTRTestClusterClusterTestListInt8UArgumentRequestParams) async throws -> MTRTestClusterClusterBooleanResponseParams
```

```objc
- (void) testListInt8UArgumentRequestWithParams:(MTRTestClusterClusterTestListInt8UArgumentRequestParams *) params completionHandler:(void (^)(MTRTestClusterClusterBooleanResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertestcluster/testlistint8uargumentrequest(with:completionhandler:))*