# credentialID

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An identifier that the authenticator generates during registration to uniquely identify a specific credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var credentialID: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * credentialID;
```

## See Also

### Getting the properties
- [var rawClientDataJSON: Data](./rawclientdatajson.md)
  Raw data that contains a JSON-compatible encoding of the client data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspublickeycredential/credentialid)*