# ErrorResponse.Errors

**Framework**: Enterprise Program API  
**Kind**: dictionary

The details about an error that are returned when an API request isn’t successful.

## Declaration

```swift
object ErrorResponse.Errors
```

#### Discussion

Use the `code` parameter for programmatic error handling. See [`Parsing the Error Response Code`](parsing-the-error-response-code.md) for more information. For more information about using the `source` parameter, see [`Pinpointing the Location of Errors`](pinpointing-the-location-of-errors.md).

## Topics

### Objects
- [object JsonPointer](jsonpointer.md)
  An object that contains the JSON pointer that indicates the location of the error.
- [object Parameter](parameter.md)
  An object that contains the query parameter that produced the error.
- [object ErrorResponse.Errors.Meta](errorresponse/errors-data.dictionary/meta-data.dictionary.md)
  An object that contains the error itself or associated errors.

## Properties

- `code` (string) *(required)*: A machine-readable code indicating the type of error. The code is a hierarchical value with levels of specificity separated by the ‘`.`’ character. This value is parseable for programmatic error handling in code.
- `status` (string) *(required)*: The HTTP status code of the error. This status code usually matches the response’s status code; however, if the request produces multiple errors, these two codes may differ.
- `id` (string): The unique ID of a specific instance of an error, request, and response. Use this ID when providing feedback to or debugging issues with Apple.
- `title` (string) *(required)*: A summary of the error. Do not use this field for programmatic error handling.
- `detail` (string) *(required)*: A detailed explanation of the error. Do not use this field for programmatic error handling.
- `source` (*): One of two possible types of values: `source.Parameter`, provided when a query parameter produced the error, or `source.JsonPointer`, provided when a problem with the entity produced the error.
- `links` (ErrorLinks)
- `meta` (ErrorResponse.Errors.Meta)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/errorresponse/errors-data.dictionary)*