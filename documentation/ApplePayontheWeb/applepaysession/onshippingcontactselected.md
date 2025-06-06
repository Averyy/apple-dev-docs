# onshippingcontactselected

**Framework**: Applepayontheweb  
**Kind**: property

An event handler to call when the user selects a shipping contact in the payment sheet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute EventHandler onshippingcontactselected;
```

#### Discussion

This attribute must be set to a function that accepts an `events` argument; for example,

`session.onshippingcontactselected = function(event) {}`.

The `event` parameter contains the [`shippingContact`](applepayshippingcontactselectedevent/shippingcontact.md) attribute. Access this attribute using the `event` parameter, for example,

`var myShippingContact = event.shippingContact;`

The [`onshippingcontactselected`](applepaysession/onshippingcontactselected.md) function must respond by calling [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) before the 30 second timeout, after which a message appears stating that the payment could not be completed.

The [`shippingContact`](applepaypayment/shippingcontact.md) attribute contains the information you requested by specifying [`requiredShippingContactFields`](applepaypaymentrequest/requiredshippingcontactfields.md) in [`ApplePayPaymentRequest`](applepaypaymentrequest.md).

Before the user authorizes the transaction, you receive redacted shipping contact information in a callback event. The redacted information includes only the necessary data for completing transaction tasks, such as calculating taxes or shipping costs.

Listing 1. An example of redacted shipping contact information

```javascript
{
    "locality": "Cupertino",
    "country": "United States",
    "postalCode": "95014",
    "administrativeArea": "CA",
    "countryCode": "us"
}
```

> **Note**:  The data returned may differ based on the user’s geographic region. For Canada and United Kingdom, a redacted shipping address excludes the  last three characters of the postal code.  For US addresses, the redacted zip code contains the first five digits. The full postal code is provided after the user authorizes the transaction.

## See Also

- [completeShippingContactSelection](applepaysession/completeshippingcontactselection.md)
  Completes the selection of a shipping contact with an update.
- [ApplePayShippingContactSelectedEvent](applepayshippingcontactselectedevent.md)
  An event object that contains the shipping address the user selects.
- [ApplePayShippingContactUpdate](applepayshippingcontactupdate.md)
  Updated transaction details that result from a change in shipping contact, including any errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/onshippingcontactselected)*