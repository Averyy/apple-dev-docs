# completeRegistrationRequest(using:completionHandler:)

**Framework**: Authentication Services  
**Kind**: method

Complete the registration request by providing the newly-created passkey credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func completeRegistrationRequest(using credential: ASPasskeyRegistrationCredential) async -> Bool
```

#### Discussion

The synchronous version of this method calls its completion handler with [`background`](https://developer.apple.com/documentation/Dispatch/DispatchQoS/background) priority.

## Parameters

- `credential`: The credential your extension created in response to the registration request.
- `completionHandler`: An optional block your extension can provide to perform any cleanup work after the system has used the credential. The expired parameter is   if the system decides to prematurely end a previous non-expiration invocation of the completion handler.

## See Also

- [func completeRequest(withSelectedCredential: ASPasswordCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:).md)
  Provides the user-selected credential.
- [func completeAssertionRequest(using: ASPasskeyAssertionCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md)
  Complete the passkey assertion request by providing the user-selected passkey credential.
- [func completeOneTimeCodeRequest(using: ASOneTimeCodeCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeonetimecoderequest(using:completionhandler:).md)
  Provides the user-selected one-time passcode (OTP).
- [class ASPasswordCredential](aspasswordcredential.md)
  A password credential.
- [class ASPasskeyAssertionCredential](aspasskeyassertioncredential.md)
  A passkey assertion credential.
- [class ASPasskeyRegistrationCredential](aspasskeyregistrationcredential.md)
  A passkey registration credential.
- [class ASOneTimeCodeCredential](asonetimecodecredential.md)
  A one-time passcode (OTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext/completeregistrationrequest(using:completionhandler:))*