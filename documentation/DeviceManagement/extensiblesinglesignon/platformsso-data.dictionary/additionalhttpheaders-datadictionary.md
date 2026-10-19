# ExtensibleSingleSignOn.PlatformSSO.AdditionalHTTPHeaders

**Framework**: Device Management  
**Kind**: dictionary

A dictionary with keys and values that are strings. The keys are HTTP header names, and the values are HTTP header values. The device adds these headers to nonce, pre-authentication, login, key and key exchange requests for Platform SSO. The device limits the number of headers to 20, the length of the header name to 128 characters, and the length of the header value to 2048 characters.

**Availability**:
- macOS 27.2+

## Declaration

```swift
object ExtensibleSingleSignOn.PlatformSSO.AdditionalHTTPHeaders
```

## Properties

- `ANY` (string): Keys and values to pass as HTTP headers to the identity provider.

## See Also

- [object ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups](extensiblesinglesignon/platformsso-data.dictionary/authorizationgroups-data.dictionary.md)
  The pairing of Authorization Rights to group names.
- [object ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping](extensiblesinglesignon/platformsso-data.dictionary/tokentousermapping-data.dictionary.md)
  The attribute mapping to use when creating users, or for authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon/platformsso-data.dictionary/additionalhttpheaders-data.dictionary)*