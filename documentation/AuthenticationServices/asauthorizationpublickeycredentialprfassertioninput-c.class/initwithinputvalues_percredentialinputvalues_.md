# initWithInputValues:perCredentialInputValues:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Initializes the inputs for the PRF extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
- (instancetype) initWithInputValues:(ASAuthorizationPublicKeyCredentialPRFAssertionInputValues *) inputValues perCredentialInputValues:(NSDictionary<NSData *,ASAuthorizationPublicKeyCredentialPRFAssertionInputValues *> *) perCredentialInputValues;
```

## Parameters

- `inputValues`: The default inputs to use for generating the PRF.
- `perCredentialInputValues`: This optional dictionary maps `credentialID` values to alternate input values. If the user selects a passkey with a `credentialID` that matches one of these keys, the extension uses the corresponding input values instead of those from the first argument. When specifying a nonempty value here, the request uses `allowedCredentials`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-c.class/initwithinputvalues:percredentialinputvalues:)*