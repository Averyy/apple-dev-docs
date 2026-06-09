# GetSubscriptionsResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains the requested subscriptions.

## Declaration

```swift
object GetSubscriptionsResponse
```

## Topics

### Objects and Data Types
- [object ResponseSubscription](responsesubscription.md)
  A subscription with its assignment counts.

## Properties

- `subscriptions` ([ResponseSubscription]): The set of requested subscriptions.
- `nextCursor` (string): The cursor for fetching the next page of results.
- `tokenExpirationDate` (string): The token expiration date in an ISO-8601 format. Note: The server shows all dates and times in UTC.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates and avoid double-counting records when different content managers upload duplicate tokens.
- `versionId` (string): The current version identifier.

## See Also

- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getsubscriptionsresponse)*