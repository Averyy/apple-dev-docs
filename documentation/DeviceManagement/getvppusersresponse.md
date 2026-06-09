# GetVppUsersResponse

**Framework**: Device Management  
**Kind**: dictionary

The response from the users’ details service.

**Availability**:
- VPP License Management 1.0+

## Declaration

```swift
object GetVppUsersResponse
```

## Properties

- `batchCount` (int32): The number of users returned in the current batch. See [`Handle batched responses`](retrieving-a-large-record-set#Handle-batched-responses.md) for more information.
- `batchToken` (string): Use this `batchToken` value in subsequent requests to get the next batch. The server generates the `batchToken` value, and it can be several kilobytes in size. For an initial request that doesn’t include `batchToken` or `sinceModifiedToken`, a `batchToken` value returns if the number of results exceeds a server-controlled limit. Subsequent requests must include `batchToken`. As long as additional batches remain, the server returns a new `batchToken` value in its response. See [`Handle batched responses`](retrieving-a-large-record-set#Handle-batched-responses.md) for more information.
- `clientContext` (string): The value currently associated with the provided `sToken`. This field is only included in the response when a value is set with the [`Client Configuration`](client-configuration.md) endpoint.
- `errorMessage` (string): The human-readable explanation of the error.
- `errorNumber` (int32): The numeric code of the error.
- `expirationMillis` (int64): The UNIX epoch timestamp, in milliseconds, when the account’s `sToken` or password expires (whichever is earlier).
- `location` (VppLocation): The location associated with the provided `sToken`. This field only returns when using a location token with an Apple School Manager account.
- `sinceModifiedToken` (string): A token that marks a place in time. After all users return for a request, the server includes a `sinceModifiedToken` value in the response. Use it in subsequent requests to get users modified after generating the token. See [`Track changes`](retrieving-a-large-record-set#Track-changes.md) for more information.
- `status` (int32): The status code for the response. Possible values are: - `0` = Success.
- `-1` = Failure.
- `totalBatchCount` (string): The total number of round trips needed to get the complete result set. See [`Handle batched responses`](retrieving-a-large-record-set#Handle-batched-responses.md) for more information.
- `totalCount` (int32): An estimate of the total number of users that will return. This value returns for requests that don’t include `batchToken`, and for the request that starts the batch process (the listing request issued with no tokens). The actual number of users that return can be different by the time the client finishes retrieving all records.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates. In this way, you can avoid double counting records when duplicate tokens are uploaded by different content managers.
- `users` ([VppUser]): A list of users managed by the provided `sToken`.

## See Also

- [object GetVppUsersRequest](getvppusersrequest.md)
  The request for the users’ details service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getvppusersresponse)*