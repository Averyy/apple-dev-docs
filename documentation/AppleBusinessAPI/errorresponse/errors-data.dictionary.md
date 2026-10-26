# ErrorResponse.Errors

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The details about an error that returns when an API request isn’t successful.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object ErrorResponse.Errors
```

## Topics

### Dictionaries
- [object ErrorResponse.Errors.Meta](./errors-data.dictionary/meta-data.dictionary.md)

## Properties

- `code` (string) *(required)*: A machine-readable code indicating the type of error. The code is a hierarchical value with levels of specificity separated by a period (.). This value is parseable for programmatic error handling in code.
- `detail` (string) *(required)*: A detailed explanation of the error. Don’t use this field for programmatic error handling.
- `id` (string): The unique ID of a specific instance of an error, request, and response. Use this ID when providing feedback to, or debugging issues with, Apple.
- `source` ((JsonPointer | Parameter)): One of two possible types of values — `source.Parameter` when a query parameter produces the error, or `source.JsonPointer` when a problem with the entity produces the error.

  **Allowed Types**: `JsonPointer`, `Parameter`
- `status` (string) *(required)*: The HTTP status code of the error. This status code usually matches the response’s status code. However, if the request produces multiple errors, these two codes may differ.
- `title` (string) *(required)*: A summary of the error. Don’t use this field for programmatic error handling.
- `links` (ErrorLinks)
- `meta` (ErrorResponse.Errors.Meta)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/errorresponse/errors-data.dictionary)*