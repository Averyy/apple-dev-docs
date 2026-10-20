# testNestedStructArgumentRequest(with:expectedValues:expectedValueInterval:completion:)

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
func testNestedStructArgumentRequest(with params: MTRUnitTestingClusterTestNestedStructArgumentRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRUnitTestingClusterBooleanResponseParams?, (any Error)?) -> Void)
```

```swift
func testNestedStructArgumentRequest(with params: MTRUnitTestingClusterTestNestedStructArgumentRequestParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRUnitTestingClusterBooleanResponseParams
```

```objc
- (void) testNestedStructArgumentRequestWithParams:(MTRUnitTestingClusterTestNestedStructArgumentRequestParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRUnitTestingClusterBooleanResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterunittesting/testnestedstructargumentrequest(with:expectedvalues:expectedvalueinterval:completion:))*