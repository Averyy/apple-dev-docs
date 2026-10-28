# cancelRequest(with:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

Command CancelMessagesRequest

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
func cancelRequest(with params: MTRMessagesClusterCancelMessagesRequestParams, completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func cancelRequest(with params: MTRMessagesClusterCancelMessagesRequestParams) async throws
```

```objc
- (void) cancelMessagesRequestWithParams:(MTRMessagesClusterCancelMessagesRequestParams *) params completion:(MTRStatusCompletion) completion;
```

## Discussion

This command will cancel the message IDs specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustermessages/cancelrequest(with:completion:))*