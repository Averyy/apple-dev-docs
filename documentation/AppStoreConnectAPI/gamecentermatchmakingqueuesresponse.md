# GameCenterMatchmakingQueuesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that get multiple queues.

**Availability**:
- App Store Connect API 3.1+

## Declaration

```swift
object GameCenterMatchmakingQueuesResponse
```

## Properties

- `data` ([GameCenterMatchmakingQueue]) *(required)*: The queues that the endpoint fetches.
- `included` ([GameCenterMatchmakingRuleSet]): The rule sets included in the response.
- `links` (PagedDocumentLinks) *(required)*: The link representations of the response.
- `meta` (PagingInformation)

## See Also

- [object GameCenterMatchmakingQueueCreateRequest](gamecentermatchmakingqueuecreaterequest.md)
  The request body you use to create a queue.
- [object GameCenterMatchmakingQueueUpdateRequest](gamecentermatchmakingqueueupdaterequest.md)
  The request body you use to modify a queue.
- [object GameCenterMatchmakingQueueResponse](gamecentermatchmakingqueueresponse.md)
  The response body for endpoints that create, modify, or get a single queue.
- [object GameCenterMatchmakingQueue](gamecentermatchmakingqueue.md)
  A queue in Game Center matchmaking that holds players waiting to be matched, governed by a rule set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/gamecentermatchmakingqueuesresponse)*