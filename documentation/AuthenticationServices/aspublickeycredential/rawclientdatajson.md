# rawClientDataJSON

**Framework**: Authentication Services  
**Kind**: property  
**Required**: Yes

Raw data that contains a JSON-compatible encoding of the client data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var rawClientDataJSON: Data { get }
```

#### Discussion

This object acts as an input to the signing algorithm. It needs to be in JSON form for the relying party to verify the provided signature. The developer should ignore this value.

## See Also

- [var credentialID: Data](aspublickeycredential/credentialid.md)
  An identifier that the authenticator generates during registration to uniquely identify a specific credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspublickeycredential/rawclientdatajson)*