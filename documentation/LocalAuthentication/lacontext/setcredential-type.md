# setCredential(_:type:)

**Framework**: Local Authentication  
**Kind**: method

Sets an application-provided credential to be used when evaluating authentication.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func setCredential(_ credential: Data?, type: LACredentialType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the credential was set, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `credential`: Setting this parameter to   removes any existing credential of the specified type.
- `type`: The type of the specified credential. For possible values, see  .

## See Also

- [func isCredentialSet(LACredentialType) -> Bool](lacontext/iscredentialset(_:).md)
  Returns a Boolean value indicating whether the specified credential type is set.
- [enum LACredentialType](lacredentialtype.md)
  The types of credentials to be used for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/setcredential(_:type:))*