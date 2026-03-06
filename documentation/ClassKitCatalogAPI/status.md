# Status

**Framework**: ClassKit Catalog API  
**Kind**: dictionary

The state of a request that the API previously accepted, but didn’t complete right away.

**Availability**:
- ClassKit 1.0+

## Declaration

```swift
object Status
```

## Topics

### Errors
- [object Status.Error](status/error-data.dictionary.md)
  Information that explains why a request failed.

## Properties

- `location` (string): The URL used to retrieve this status.
- `state` (string): The state of the request.
- `teamId` (string): The identifier of the team associated with this status.
- `statusId` (string): The unique value that identifies this status.
- `error` (Status.Error): Information that the system provides for a request that fails.
- `statusCode` (string): A response code that indicates the outcome of the request.

## See Also

- [Get Status](get-status.md)
  Fetch the status of an operation that you initiated earlier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/status)*