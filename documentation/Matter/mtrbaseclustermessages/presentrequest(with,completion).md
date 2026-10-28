# presentRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command PresentMessagesRequest

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
func presentRequest(with params: MTRMessagesClusterPresentMessagesRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func presentRequest(with params: MTRMessagesClusterPresentMessagesRequestParams) async throws
```

```objc
- (void) presentMessagesRequestWithParams:(MTRMessagesClusterPresentMessagesRequestParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

Upon receipt, this SHALL cause the message in the passed fields to be appended to the Messages attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermessages/presentrequest(with:completion:))*