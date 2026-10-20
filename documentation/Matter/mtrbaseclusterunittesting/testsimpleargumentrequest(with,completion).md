# testSimpleArgumentRequest(with:completion:)

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
func testSimpleArgumentRequest(with params: MTRUnitTestingClusterTestSimpleArgumentRequestParams, completion: @escaping @Sendable (MTRUnitTestingClusterTestSimpleArgumentResponseParams?, (any Error)?) -> Void)
```

```swift
func testSimpleArgumentRequest(with params: MTRUnitTestingClusterTestSimpleArgumentRequestParams) async throws -> MTRUnitTestingClusterTestSimpleArgumentResponseParams
```

```objc
- (void) testSimpleArgumentRequestWithParams:(MTRUnitTestingClusterTestSimpleArgumentRequestParams *) params completion:(void (^)(MTRUnitTestingClusterTestSimpleArgumentResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterunittesting/testsimpleargumentrequest(with:completion:))*