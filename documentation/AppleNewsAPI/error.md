# Error

**Framework**: AppleNewsAPI  
**Kind**: dictionary  
**Role**: Object

See the properties of an error the Apple News API returned.

**Availability**:
- Apple News API 1.0+

## Declaration

```
object Error
```

## Mentions

- [Getting Ready to Publish and Manage Your Articles](../AppleNews/getting-ready-to-publish-and-manage-your-articles.md)

## Properties

- `code` (Code): An error code that, in combination with the key path, uniquely identifies the error for the specified endpoint.

  Returned: Always
- `keyPath` ([string]): An array of field names that uniquely identifies a field in the JSON input of the request. See [Understanding the keyPath Array](../AppleNews/about-apple-news-api-error-messages.md#Understanding-the-keyPath-Array).

  Returned: Sometimes
- `message` (string): A user-friendly, detailed explanation of the error code.

  Returned: Sometimes
- `status` (Status): A code the server issues in response to a request.

  Returned: Always
- `value` (string): If applicable, the value supplied in the request for the field that `keyPath` specifies.

  Returned: Sometimes

## See Also

### Errors
- [About Apple News API Error Messages](../AppleNews/about-apple-news-api-error-messages.md)
  Understand the error message format for the Apple News API.
- [object Warning](./warning.md)
  See the properties of a warning the Apple News API returned.
- [type Code](./code.md)
  See the error codes the Apple News API returned.
- [type Status](./status.md)
  See the HTTP status codes the Apple News API returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/error)*