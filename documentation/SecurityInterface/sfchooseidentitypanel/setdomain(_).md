# setDomain(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets an optional domain in which the identity is to be used.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setDomain(_ domainString: String!)
```

```objc
- (void) setDomain:(NSString *) domainString;
```

#### Discussion

Call this method to associate a domain with the chosen identity. If the user chooses an identity and a domain is set, an identity preference item is created in the default keychain. Subsequent calls to  [`SecIdentitySearchCreate`](../../Security/secidentitysearchcreate.md) and [`SecIdentitySearchCopyNext`](../../Security/secidentitysearchcopynext.md) return the preferred identity for this domain first.

## Parameters

- `domainString`: A string containing a hostname, RFC 822 name (email address), URL, or similar identifier.

## See Also

### Working with Domains
- [func domain() -> String!](./domain%28%29.md)
  Returns the domain that will be associated with the chosen identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setdomain(_:))*