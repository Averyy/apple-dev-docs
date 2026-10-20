# ErrorLinks

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Navigation links within an error response, providing references to related resources or documentation.

**Availability**:
- App Store Connect API 3.5+

## Declaration

```
object ErrorLinks
```

## Topics

### Objects
- [object ErrorLinks.Associated](./errorlinks/associated-data.dictionary.md)
  The associated resource links within an error’s navigation links.

## Properties

- `about` (uri-reference)
- `associated` (*): **Allowed Types**: `uri-reference`, `ErrorLinks.Associated`

## See Also

### Objects
- [object ErrorResponse](./errorresponse.md)
  The error details that an API returns in the response body whenever the API request isn’t successful.
- [object JsonPointer](./jsonpointer.md)
  An object that contains the JSON pointer that indicates the location of the error.
- [object Parameter](./parameter.md)
  An object that contains the query parameter that produced the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/errorlinks)*