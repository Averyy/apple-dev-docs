# JsonPointer

**Framework**: App Store Connect API  
**Kind**: dictionary

An object that contains the JSON pointer that indicates the location of the error.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object JsonPointer
```

#### Discussion

In some cases, the JSON pointer may indicate an element that isn’t in the request entity, but should be. For more information about JSON pointers, see the [`RFC 6901`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6901) proposed standards document.

## Properties

- `pointer` (string) *(required)*: A JSON pointer that indicates the location in the request entity where the error originates.

## See Also

- [object ErrorLinks](errorlinks.md)
  Navigation links within an error response, providing references to related resources or documentation.
- [object ErrorResponse](errorresponse.md)
  The error details that an API returns in the response body whenever the API request isn’t successful.
- [object Parameter](parameter.md)
  An object that contains the query parameter that produced the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/jsonpointer)*