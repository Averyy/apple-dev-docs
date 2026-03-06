# Error

**Framework**: Apple Music API  
**Kind**: dictionary

Information about an error that occurred while processing a request.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object Error
```

## Mentions

- [Handling Requests and Responses](handling-requests-and-responses.md)
- [HTTP Status Codes](http-status-codes.md)

#### Discussion

If a request is unsuccessful, the `errors` in the response may contain an Error object for each problem that occurred.

## Topics

### Related Objects
- [object Error.Source](error/source-data.dictionary.md)
  The Source object represents the source of an error.

## Properties

- `code` (string) *(required)*: The code for this error. For possible values, see [`HTTP Status Codes`](http-status-codes.md).
- `detail` (string): A long, possibly localized, description of the problem.
- `id` (string) *(required)*: A unique identifier for this occurrence of the error.
- `source` (Error.Source): An object containing references to the source of the error. For possible members, see `Source` object.
- `status` (string) *(required)*: The HTTP status code for this problem.
- `title` (string) *(required)*: A short, possibly localized, description of the problem.

## See Also

- [HTTP Status Codes](http-status-codes.md)
  Reference error codes returned by the Apple Music API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/error)*