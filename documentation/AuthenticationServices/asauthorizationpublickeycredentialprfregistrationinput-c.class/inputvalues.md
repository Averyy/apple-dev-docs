# inputValues

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The input values to use when generating the PRF extension, if specified.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) ASAuthorizationPublicKeyCredentialPRFAssertionInputValues * inputValues;
```

#### Discussion

If this property isn’t specified, the output only indicates whether there’s support for the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationinput-c.class/inputvalues)*