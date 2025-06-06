# saltInput1(_:saltInput2:)

**Framework**: Authentication Services  
**Kind**: method

The inputs for generating the PRF output secrets.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func saltInput1(_ saltInput1: Data, saltInput2: Data? = nil) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues
```

#### Return Value

A configured instance of `InputValues`.

## Parameters

- `saltInput1`: The input used when generating  .
- `saltInput2`: If specified, the input when generating  . If not specified,   will be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct/saltinput1(_:saltinput2:))*