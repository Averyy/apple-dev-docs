# signature(for:using:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

Signs the supplied array of data with the identity’s private key

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func signature(for data: [Data], using request: JPKIPassContents.AuthenticationRequest<Self.IdentityType>) async throws -> [JPKIPassContents.Signature<Self.IdentityType>]
```

#### Discussion

- Properties: - data: Data array to be signed with the specified identity
- authentication: User authentication request to perform identity signature with

> **Note**: See Error type defined below

See Error type defined below


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/identity/signature(for:using:)-35arv)*