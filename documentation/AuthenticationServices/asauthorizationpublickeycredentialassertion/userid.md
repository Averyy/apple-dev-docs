# userID

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A user identifier for the assertion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var userID: Data! { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * userID;
```

## See Also

### Getting the properties
- [var signature: Data!](./signature.md)
  The signature for the assertion.
- [var rawAuthenticatorData: Data!](./rawauthenticatordata.md)
  A byte sequence that contains additional information about the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertion/userid)*