# setDomain(_:)

**Framework**: Security Interface  
**Kind**: method

Sets an optional domain in which the identity is to be used.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setDomain(_ domainString: String!)
```

#### Discussion

Call this method to associate a domain with the chosen identity. If the user chooses an identity and a domain is set, an identity preference item is created in the default keychain. Subsequent calls to  [`SecIdentitySearchCreate`](https://developer.apple.com/documentation/Security/SecIdentitySearchCreate) and [`SecIdentitySearchCopyNext`](https://developer.apple.com/documentation/Security/SecIdentitySearchCopyNext) return the preferred identity for this domain first.

## Parameters

- `domainString`: A string containing a hostname, RFC 822 name (email address), URL, or similar identifier.

## See Also

- [func domain() -> String!](sfchooseidentitypanel/domain.md)
  Returns the domain that will be associated with the chosen identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setdomain(_:))*