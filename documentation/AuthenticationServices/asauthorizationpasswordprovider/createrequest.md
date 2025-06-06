# createRequest()

**Framework**: Authentication Services  
**Kind**: method

Creates a new password authorization request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func createRequest() -> ASAuthorizationPasswordRequest
```

#### Return Value

A password authorization request that you can execute with an instance of [`ASAuthorizationController`](asauthorizationcontroller.md).

## See Also

- [class ASAuthorizationPasswordRequest](asauthorizationpasswordrequest.md)
  An authorization request that uses credentials stored in the keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpasswordprovider/createrequest())*