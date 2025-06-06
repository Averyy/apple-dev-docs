# credentialID

**Framework**: Authentication Services  
**Kind**: property

The credential identifier for this passkey credential identity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var credentialID: Data { get }
```

#### Discussion

Use the credential identifier, along with the [`userHandle`](aspasskeycredentialidentity/userhandle.md), to identify the correct credential to use for a given relying party request.

## See Also

- [var recordIdentifier: String?](aspasskeycredentialidentity/recordidentifier.md)
  A string used to correlate this identity to a record in your app’s own database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialidentity/credentialid)*