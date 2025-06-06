# ErrorResponse.Errors

**Framework**: App Store Connect API  
**Kind**: dictionary

The details about an error that are returned when an API request isn’t successful.

**Availability**:
- App Store Connect API 1.0+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/errorresponse/errors-data.dictionary)*