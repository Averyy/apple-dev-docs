# testListInt8UReverseRequest(with:completion:)

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
func testListInt8UReverseRequest(with params: MTRUnitTestingClusterTestListInt8UReverseRequestParams, completion: @escaping @Sendable (MTRUnitTestingClusterTestListInt8UReverseResponseParams?, (any Error)?) -> Void)
```

```swift
func testListInt8UReverseRequest(with params: MTRUnitTestingClusterTestListInt8UReverseRequestParams) async throws -> MTRUnitTestingClusterTestListInt8UReverseResponseParams
```

```objc
- (void) testListInt8UReverseRequestWithParams:(MTRUnitTestingClusterTestListInt8UReverseRequestParams *) params completion:(void (^)(MTRUnitTestingClusterTestListInt8UReverseResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterunittesting/testlistint8ureverserequest(with:completion:))*