# testNullableOptionalRequest(with:completion:)

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
func testNullableOptionalRequest(with params: MTRUnitTestingClusterTestNullableOptionalRequestParams?, completion: @escaping @Sendable (MTRUnitTestingClusterTestNullableOptionalResponseParams?, (any Error)?) -> Void)
```

```swift
func testNullableOptionalRequest(with params: MTRUnitTestingClusterTestNullableOptionalRequestParams?) async throws -> MTRUnitTestingClusterTestNullableOptionalResponseParams
```

```objc
- (void) testNullableOptionalRequestWithParams:(MTRUnitTestingClusterTestNullableOptionalRequestParams *) params completion:(void (^)(MTRUnitTestingClusterTestNullableOptionalResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterunittesting/testnullableoptionalrequest(with:completion:))*