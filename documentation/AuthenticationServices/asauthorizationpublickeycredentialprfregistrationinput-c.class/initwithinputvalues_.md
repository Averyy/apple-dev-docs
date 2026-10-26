# initWithInputValues:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Initializes a registration input object with inputs for the PRF extension to evaluate if the new passkey supports the extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
- (instancetype) initWithInputValues:(ASAuthorizationPublicKeyCredentialPRFAssertionInputValues *) inputValues;
```

## Parameters

- `inputValues`: The inputs to use for generating the PRF.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-c.class/initwithinputvalues:)*