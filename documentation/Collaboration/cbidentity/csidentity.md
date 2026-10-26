# CSIdentity

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns an opaque object for use with the Core Services Identity API.

**Availability**:
- macOS 10.5+

## Declaration

```objc
@property (readonly) CSIdentityRef CSIdentity;
```

#### Return Value

The opaque object for use with the Core Services Identity API.

#### Discussion

This method, along with [`identityWithCSIdentity:`](./identitywithcsidentity_.md), is used for interoperability with the Core Services Identity API.

## See Also

### Storing Identities
- [var persistentReference: Data?](./persistentreference.md)
  Returns a persistent reference to store a reference to an identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/csidentity)*