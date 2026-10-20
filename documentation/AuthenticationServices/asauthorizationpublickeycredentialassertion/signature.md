# signature

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The signature for the assertion.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var signature: Data! { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * signature;
```

## See Also

### Getting the properties
- [var userID: Data!](./userid.md)
  A user identifier for the assertion.
- [var rawAuthenticatorData: Data!](./rawauthenticatordata.md)
  A byte sequence that contains additional information about the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertion/signature)*