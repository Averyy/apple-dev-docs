# Status.Error

**Framework**: ClassKit Catalog API  
**Kind**: dictionary

Information that explains why a request failed.

**Availability**:
- ClassKit 1.0+

## Declaration

```swift
object Status.Error
```

## Properties

- `code` (string): A brief code that identifies the kind of error.
- `id` (string): The `statusId` of the request that caused the error, as described in [`Get Status`](get-status.md).
- `message` (string): A human readable explanation for the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/status/error-data.dictionary)*