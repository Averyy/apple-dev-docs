# GameCenterMatchmakingQueueResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, modify, or get a single queue.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingQueueResponse
```

## Properties

- `data` (GameCenterMatchmakingQueue) *(required)*: The queue that you create, modify, or get.
- `included` ([GameCenterMatchmakingRuleSet]): The rule sets included in the response.
- `links` (DocumentLinks) *(required)*: The link representations of the response.

## See Also

- [object GameCenterMatchmakingQueueCreateRequest](gamecentermatchmakingqueuecreaterequest.md)
  The request body you use to create a queue.
- [object GameCenterMatchmakingQueueUpdateRequest](gamecentermatchmakingqueueupdaterequest.md)
  The request body you use to modify a queue.
- [object GameCenterMatchmakingQueuesResponse](gamecentermatchmakingqueuesresponse.md)
  The response body for endpoints that get multiple queues.
- [object GameCenterMatchmakingQueue](gamecentermatchmakingqueue.md)
  The data structure that represents a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingqueueresponse)*