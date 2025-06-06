# init(encryptionScheme:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Instantiates a new request configuration with the given encryption scheme.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(encryptionScheme: PKEncryptionScheme)
```

#### Return Value

A newly instantiated configuration object.

#### Discussion

After instantiating a configuration object, you must also set its [`cardholderName`](pkaddpaymentpassrequestconfiguration/cardholdername.md) and [`primaryAccountSuffix`](pkaddpaymentpassrequestconfiguration/primaryaccountsuffix.md) properties before using it to create a [`PKAddPaymentPassViewController`](pkaddpaymentpassviewcontroller.md) instance.

## Parameters

- `encryptionScheme`: The encryption scheme to be used in this request. For a list of possible values, see  .

## See Also

- [struct PKEncryptionScheme](pkencryptionscheme.md)
  Encryption schemes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/init(encryptionscheme:))*