# inputValues

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The input values to use when generating the PRF extension output, if specified.

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

## Discussion

When also using [`perCredentialInputValues`](./percredentialinputvalues.md), you may use the corresponding value from that dictionary instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-c.class/inputvalues)*