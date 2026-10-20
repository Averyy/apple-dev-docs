# testAddArguments(with:completion:)

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
func testAddArguments(with params: MTRUnitTestingClusterTestAddArgumentsParams, completion: @escaping @Sendable (MTRUnitTestingClusterTestAddArgumentsResponseParams?, (any Error)?) -> Void)
```

```swift
func testAddArguments(with params: MTRUnitTestingClusterTestAddArgumentsParams) async throws -> MTRUnitTestingClusterTestAddArgumentsResponseParams
```

```objc
- (void) testAddArgumentsWithParams:(MTRUnitTestingClusterTestAddArgumentsParams *) params completion:(void (^)(MTRUnitTestingClusterTestAddArgumentsResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterunittesting/testaddarguments(with:completion:))*