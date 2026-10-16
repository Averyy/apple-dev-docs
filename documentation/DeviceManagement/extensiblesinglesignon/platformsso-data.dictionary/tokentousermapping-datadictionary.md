# ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping

**Framework**: Device Management  
**Kind**: dictionary

The attribute mapping to use when creating users, or for authorization.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping
```

## Properties

- `AccountName` (string): The claim name to use for the user’s account name.
- `FullName` (string): The claim name to use for the user’s full name.

## See Also

- [object ExtensibleSingleSignOn.PlatformSSO.AdditionalHTTPHeaders](extensiblesinglesignon/platformsso-data.dictionary/additionalhttpheaders-data.dictionary.md)
  A dictionary with keys and values that are strings. The keys are HTTP header names, and the values are HTTP header values. The device adds these headers to nonce, pre-authentication, login, key and key exchange requests for Platform SSO. The device limits the number of headers to 20, the length of the header name to 128 characters, and the length of the header value to 2048 characters.
- [object ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups](extensiblesinglesignon/platformsso-data.dictionary/authorizationgroups-data.dictionary.md)
  The pairing of Authorization Rights to group names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon/platformsso-data.dictionary/tokentousermapping-data.dictionary)*