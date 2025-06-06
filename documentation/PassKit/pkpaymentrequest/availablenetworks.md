# availableNetworks()

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns the list of available payment methods that Apple Pay supports.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func availableNetworks() -> [PKPaymentNetwork]
```

#### Return Value

An array of strings representing the available payment networks. For a list of possible networks, see [`PKPaymentNetwork`](pkpaymentnetwork.md).

#### Discussion

To dynamically select the payment networks at runtime, use this method to get the complete list of currently supported networks. You can then filter this list, as needed, and assign the results to the payment request’s [`supportedNetworks`](pkpaymentrequest/supportednetworks.md) property.

## See Also

- [Wallet Developer Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)
- [var supportedNetworks: [PKPaymentNetwork]](pkpaymentrequest/supportednetworks.md)
  The payment methods that you support.
- [struct PKPaymentNetwork](pkpaymentnetwork.md)
  A type that represents a payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/availablenetworks())*