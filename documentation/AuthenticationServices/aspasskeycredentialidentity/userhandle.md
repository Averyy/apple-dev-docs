# userHandle

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The user handle of this passkey credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var userHandle: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * userHandle;
```

## Discussion

Use the user handle, along with the [`credentialID`](./credentialid.md), to identify the correct credential to use for a given relying party request.

## See Also

### Associating a user
- [var userName: String](./username.md)
  The username of this passkey credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialidentity/userhandle)*