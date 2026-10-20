# contentAppMessage(with:expectedValues:expectedValueInterval:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func contentAppMessage(with params: MTRContentAppObserverClusterContentAppMessageParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?, completion: @escaping @Sendable (MTRContentAppObserverClusterContentAppMessageResponseParams?, (any Error)?) -> Void)
```

```swift
func contentAppMessage(with params: MTRContentAppObserverClusterContentAppMessageParams, expectedValues expectedDataValueDictionaries: [[String : Any]]?, expectedValueInterval expectedValueIntervalMs: NSNumber?) async throws -> MTRContentAppObserverClusterContentAppMessageResponseParams
```

```objc
- (void) contentAppMessageWithParams:(MTRContentAppObserverClusterContentAppMessageParams *) params expectedValues:(NSArray<NSDictionary<NSString *,id> *> *) expectedDataValueDictionaries expectedValueInterval:(NSNumber *) expectedValueIntervalMs completion:(void (^)(MTRContentAppObserverClusterContentAppMessageResponseParams *data, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclustercontentappobserver/contentappmessage(with:expectedvalues:expectedvalueinterval:completion:))*