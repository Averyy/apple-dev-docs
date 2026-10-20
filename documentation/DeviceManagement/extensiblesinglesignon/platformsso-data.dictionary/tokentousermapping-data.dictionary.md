# ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The attribute mapping to use when creating users, or for authorization.

**Availability**:
- macOS 14.0+

## Declaration

```
object ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping
```

## Properties

- `AccountName` (string): The claim name to use for the user’s account name.
- `FullName` (string): The claim name to use for the user’s full name.

## See Also

### Objects
- [object ExtensibleSingleSignOn.PlatformSSO.AdditionalHTTPHeaders](./additionalhttpheaders-data.dictionary.md)
  A dictionary with keys and values that are strings. The keys are HTTP header names, and the values are HTTP header values. The device adds these headers to nonce, pre-authentication, login, key and key exchange requests for Platform SSO. The device limits the number of headers to 20, the length of the header name to 128 characters, and the length of the header value to 2048 characters.
- [object ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups](./authorizationgroups-data.dictionary.md)
  The pairing of Authorization Rights to group names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon/platformsso-data.dictionary/tokentousermapping-data.dictionary)*