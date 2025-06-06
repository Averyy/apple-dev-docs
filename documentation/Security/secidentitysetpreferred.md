# SecIdentitySetPreferred(_:_:_:)

**Framework**: Security  
**Kind**: func

Sets the identity that should be preferred for the specified name and key use.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecIdentitySetPreferred(_ identity: SecIdentity?, _ name: CFString, _ keyUsage: CFArray?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `identity`: The identity to set as preferred for the specified name and key usage.
- `name`: A string containing an email address (RFC 822) or other name for which a preferred certificate is requested.
- `keyUsage`: An array containing a list of usage attributes ( , for example), or   if you want this identity to be preferred for any usage. See Attribute Item Keys for a complete list of possible usage attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitysetpreferred(_:_:_:))*