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

## See Also

- [object Parameter](parameter.md)
  An object that contains the query parameter that produced the error.
- [object ErrorResponse.Errors.Meta](errorresponse/errors-data.dictionary/meta-data.dictionary.md)
  An object that contains the error itself or associated errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/jsonpointer)*