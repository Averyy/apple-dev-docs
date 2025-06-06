# requiredBillingContactFields

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A list of fields that you need for a billing contact to process the transaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var requiredBillingContactFields: Set<PKContactField> { get set }
```

#### Discussion

See [`PKContactField`](pkcontactfield.md) for the list of possible contact fields.

## See Also

- [var requiredShippingContactFields: Set<PKContactField>](pkpaymentrequest/requiredshippingcontactfields.md)
  A list of fields that you need for a shipping contact to process the transaction.
- [struct PKContactField](pkcontactfield.md)
  The fields that describe a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/requiredbillingcontactfields)*