# ApplePayShippingContactEditingMode

**Framework**: Apple Pay on the Web  
**Kind**: enum

Values that indicate whether the shipping mode prevents the user from editing fields of the shipping address.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayShippingContactEditingMode
```

#### Overview

The values for the contact editing mode:

> ❗ **Important**:  Previous versions of the Apple Pay JS API accepted `enabled` rather than `available` as a parameter for the `ApplePayShippingContactEditingMode`. Developers should upgrade their code to use `available`.``

## Topics

### Enumeration Cases
- [enabled](applepayshippingcontacteditingmode/enabled.md)
- [storePickup](applepayshippingcontacteditingmode/storepickup.md)

## See Also

- [requiredBillingContactFields](applepaypaymentrequest/requiredbillingcontactfields.md)
  The fields of billing information the user must provide to process the transaction.
- [requiredShippingContactFields](applepaypaymentrequest/requiredshippingcontactfields.md)
  The fields of shipping information the user must provide to fulfill the order.
- [shippingContactEditingMode](applepaypaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [ApplePayContactField](applepaycontactfield.md)
  Field names for requesting contact information in a payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontacteditingmode)*