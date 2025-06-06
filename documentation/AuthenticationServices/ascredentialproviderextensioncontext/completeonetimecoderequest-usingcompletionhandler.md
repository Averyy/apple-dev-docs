# completeOneTimeCodeRequest(using:completionHandler:)

**Framework**: Authentication Services  
**Kind**: method

Provides the user-selected one-time passcode (OTP).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func completeOneTimeCodeRequest(using credential: ASOneTimeCodeCredential) async -> Bool
```

## Mentions

- [Providing one-time passcodes to AutoFill](providing-one-time-passcodes-to-autofill.md)

#### Overview

After calling this method, the system dismisses the associated view controller.

## Parameters

- `credential`: The OTP credential chosen by the person.
- `completionHandler`: Optional work that the extension performs as a background priority task after the request completes. The   parameter is   if the system prematurely terminates a previous non-expiration invocation of the  .

## See Also

- [func completeRequest(withSelectedCredential: ASPasswordCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:).md)
  Provides the user-selected credential.
- [func completeAssertionRequest(using: ASPasskeyAssertionCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md)
  Complete the passkey assertion request by providing the user-selected passkey credential.
- [func completeRegistrationRequest(using: ASPasskeyRegistrationCredential, completionHandler: ((Bool) -> Void)?)](ascredentialproviderextensioncontext/completeregistrationrequest(using:completionhandler:).md)
  Complete the registration request by providing the newly-created passkey credential.
- [class ASPasswordCredential](aspasswordcredential.md)
  A password credential.
- [class ASPasskeyAssertionCredential](aspasskeyassertioncredential.md)
  A passkey assertion credential.
- [class ASPasskeyRegistrationCredential](aspasskeyregistrationcredential.md)
  A passkey registration credential.
- [class ASOneTimeCodeCredential](asonetimecodecredential.md)
  A one-time passcode (OTP) credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextensioncontext/completeonetimecoderequest(using:completionhandler:))*