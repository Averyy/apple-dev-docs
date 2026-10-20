# simpleStructEchoRequest(with:completion:)

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
func simpleStructEchoRequest(with params: MTRUnitTestingClusterSimpleStructEchoRequestParams, completion: @escaping @Sendable (MTRUnitTestingClusterSimpleStructResponseParams?, (any Error)?) -> Void)
```

```swift
func simpleStructEchoRequest(with params: MTRUnitTestingClusterSimpleStructEchoRequestParams) async throws -> MTRUnitTestingClusterSimpleStructResponseParams
```

```objc
- (void) simpleStructEchoRequestWithParams:(MTRUnitTestingClusterSimpleStructEchoRequestParams *) params completion:(void (^)(MTRUnitTestingClusterSimpleStructResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterunittesting/simplestructechorequest(with:completion:))*