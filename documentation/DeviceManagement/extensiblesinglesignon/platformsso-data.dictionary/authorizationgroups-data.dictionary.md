# ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The pairing of Authorization Rights to group names.

**Availability**:
- macOS 14.0+

## Declaration

```
object ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups
```

## Properties

- `ANY` (string): The key is an access right value, the value is the group to be associated with that access right.

## See Also

### Objects
- [object ExtensibleSingleSignOn.PlatformSSO.AdditionalHTTPHeaders](./additionalhttpheaders-data.dictionary.md)
  A dictionary with keys and values that are strings. The keys are HTTP header names, and the values are HTTP header values. The device adds these headers to nonce, pre-authentication, login, key and key exchange requests for Platform SSO. The device limits the number of headers to 20, the length of the header name to 128 characters, and the length of the header value to 2048 characters.
- [object ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping](./tokentousermapping-data.dictionary.md)
  The attribute mapping to use when creating users, or for authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon/platformsso-data.dictionary/authorizationgroups-data.dictionary)*