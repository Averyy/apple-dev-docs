# testStructArrayArgumentRequest(with:completion:)

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
func testStructArrayArgumentRequest(with params: MTRUnitTestingClusterTestStructArrayArgumentRequestParams, completion: @escaping @Sendable (MTRUnitTestingClusterTestStructArrayArgumentResponseParams?, (any Error)?) -> Void)
```

```swift
func testStructArrayArgumentRequest(with params: MTRUnitTestingClusterTestStructArrayArgumentRequestParams) async throws -> MTRUnitTestingClusterTestStructArrayArgumentResponseParams
```

```objc
- (void) testStructArrayArgumentRequestWithParams:(MTRUnitTestingClusterTestStructArrayArgumentRequestParams *) params completion:(void (^)(MTRUnitTestingClusterTestStructArrayArgumentResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterunittesting/teststructarrayargumentrequest(with:completion:))*