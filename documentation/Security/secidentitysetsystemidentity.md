# SecIdentitySetSystemIdentity(_:_:)

**Framework**: Security  
**Kind**: func

Assigns the system identity to be associated with a specified domain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SecIdentitySetSystemIdentity(_ domain: CFString, _ idRef: SecIdentity?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The caller must be running as root.

## Parameters

- `domain`: The domain to which the specified identity will be assigned, typically in reverse DNS notation, such as  .  You may also pass the values defined in  .
- `idRef`: The identity to be assigned to the specified domain. Pass   to delete any currently-assigned identity for the specified domain; in this case, it is not an error if no identity exists for the specified domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitysetsystemidentity(_:_:))*