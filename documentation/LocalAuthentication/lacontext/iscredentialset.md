# isCredentialSet(_:)

**Framework**: Local Authentication  
**Kind**: method

Returns a Boolean value indicating whether the specified credential type is set.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func isCredentialSet(_ type: LACredentialType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the credential is set, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `type`: The type of the credential. For possible values, see 

## See Also

- [func setCredential(Data?, type: LACredentialType) -> Bool](lacontext/setcredential(_:type:).md)
  Sets an application-provided credential to be used when evaluating authentication.
- [enum LACredentialType](lacredentialtype.md)
  The types of credentials to be used for authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/iscredentialset(_:))*