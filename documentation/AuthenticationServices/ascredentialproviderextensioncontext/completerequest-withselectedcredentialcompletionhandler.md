# completeRequest(withSelectedCredential:completionHandler:)

**Framework**: Authentication Services  
**Kind**: method

Provides the user-selected credential.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func completeRequest(withSelectedCredential credential: ASPasswordCredential, completionHandler: ((Bool) -> Void)? = nil)
```

#### Discussion

After calling this method, the system dismisses the associated view controller.

## Parameters

- `credential`: The credential that the user selected.
- `completionHandler`: Optional work that the extension performs as a background priority task after the request completes. The   parameter is   if the system prematurely terminates a previous non-expiration invocation of the  .

## See Also

- [func completeAssertionRequest(using: ASPasskeyAssertionCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md)
  Complete the passkey assertion request by providing the user-selected passkey credential.
- [func completeRegistrationRequest(using: ASPasskeyRegistrationCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeregistrationrequest(using:completionhandler:).md)
  Complete the registration request by providing the newly-created passkey credential.
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

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:))*