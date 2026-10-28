# contentAppMessage(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command ContentAppMessage

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
func contentAppMessage(with params: MTRContentAppObserverClusterContentAppMessageParams, completion: @escaping @Sendable (MTRContentAppObserverClusterContentAppMessageResponseParams?, (any Error)?) -> Void)
```

```swift
func contentAppMessage(with params: MTRContentAppObserverClusterContentAppMessageParams) async throws -> MTRContentAppObserverClusterContentAppMessageResponseParams
```

```objc
- (void) contentAppMessageWithParams:(MTRContentAppObserverClusterContentAppMessageParams *) params completion:(void (^)(MTRContentAppObserverClusterContentAppMessageResponseParams *data, NSError *error)) completion;
```

## Discussion

Upon receipt, the data field MAY be parsed and interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustercontentappobserver/contentappmessage(with:completion:))*