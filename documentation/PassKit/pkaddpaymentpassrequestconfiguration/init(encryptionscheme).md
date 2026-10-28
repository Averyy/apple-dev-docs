# init(encryptionScheme:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Instantiates a new request configuration with the given encryption scheme.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+

## Declaration

```swift
init?(encryptionScheme: PKEncryptionScheme)
```

```objc
- (instancetype) initWithEncryptionScheme:(PKEncryptionScheme) encryptionScheme;
```

## Return Value

A newly instantiated configuration object.

## Discussion

After instantiating a configuration object, you must also set its [`cardholderName`](./cardholdername.md) and [`primaryAccountSuffix`](./primaryaccountsuffix.md) properties before using it to create a [`PKAddPaymentPassViewController`](../pkaddpaymentpassviewcontroller.md) instance.

## Parameters

- `encryptionScheme`: The encryption scheme to be used in this request. For a list of possible values, see [`PKEncryptionScheme`](../pkencryptionscheme.md).

## See Also

### Creating a request configuration
- [struct PKEncryptionScheme](../pkencryptionscheme.md)
  Encryption schemes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequestconfiguration/init(encryptionscheme:))*