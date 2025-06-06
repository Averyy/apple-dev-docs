# shippingContactEditingMode

**Framework**: Apple Pay on the Web  
**Kind**: property

A value that indicates whether the shipping mode prevents the user from editing the shipping address.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayShippingContactEditingMode shippingContactEditingMode;
```

#### Discussion

Set the value to `storePickup` for an in-store or other pickup to prevent the user from editing the shipping address.

For more information on configuring a package for store pickup, see [`Displaying a Read-Only Pickup Address`](https://developer.apple.com/documentation/PassKit/displaying-a-read-only-pickup-address).

> ❗ **Important**:  Determine whether to disable editing of the shipping contact field before displaying the payment sheet. Switching from a noneditable to an editable shipping contact field requires the user to restart the payment process.

 Determine whether to disable editing of the shipping contact field before displaying the payment sheet. Switching from a noneditable to an editable shipping contact field requires the user to restart the payment process.

## See Also

- [billingContact](applepayrequestbase/billingcontact.md)
  A prepopulated billing address.
- [shippingContact](applepayrequestbase/shippingcontact.md)
  The customer’s address, used for sending products or services for to the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequestbase/shippingcontacteditingmode)*