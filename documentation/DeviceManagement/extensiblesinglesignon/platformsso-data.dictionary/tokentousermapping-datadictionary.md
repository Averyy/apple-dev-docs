# ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping

**Framework**: Device Management  
**Kind**: dictionary

The attribute mapping to use when creating users, or for authorization.

**Availability**:
- macOS 14.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ExtensibleSingleSignOn.PlatformSSO.TokenToUserMapping
```

## Properties

- `AccountName` (string): The claim name to use for the user’s account name.
- `FullName` (string): The claim name to use for the user’s full name.

## See Also

- [object ExtensibleSingleSignOn.PlatformSSO.AuthorizationGroups](extensiblesinglesignon/platformsso-data.dictionary/authorizationgroups-data.dictionary.md)
  The pairing of Authorization Rights to group names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignon/platformsso-data.dictionary/tokentousermapping-data.dictionary)*