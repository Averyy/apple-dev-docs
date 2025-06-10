# ApplePayModifier

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that defines the Apple Pay modifiers for a payment type in the W3C Payment Request API.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayModifier {
	ApplePayPaymentMethodType paymentMethodType;
	ApplePayLineItem total;
	sequence <ApplePayLineItem> additionalLineItems;
	sequence <ApplePayShippingMethod> additionalShippingMethods;
	sequence <ApplePayPaymentTokenContext> multiTokenContexts;
	ApplePayAutomaticReloadPaymentRequest automaticReloadPaymentRequest;
	ApplePayRecurringPaymentRequest recurringPaymentRequest;
	ApplePayDeferredPaymentRequest deferredPaymentRequest;
};
```

## Mentions

- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)
- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)
- [Apple Pay on the Web Version 14 Release Notes](apple-pay-on-the-web-version-14-release-notes.md)

#### Overview

This dictionary contains the supported Apple Pay properties for the `PaymentDetailsModifier` `data` object in the [`Payment Request API`](payment-request-api.md). For more information about `PaymentDetailsModifier`, see the [`W3C Payment Request API specification`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentdetailsmodifier-dictionary).

In the Payment Request API, modifiers contain transaction details that apply only under certain conditions. For example, you can create a modifier that adds a surcharge for paying with a credit card. Each transaction contains the modifier details, but the payment sheet only displays the surcharge if the user chooses to pay with a credit card.

In Apple Pay, define display items using an [`ApplePayModifier`](applepaymodifier.md) based on the user’s choice of payment method type: `"credit"`, `"debit"`, `"prepaid"`, or `"store"`. When the user selects their payment method, the transaction displays the information on the payment sheet based on the modifier corresponding to the payment method. To create a modifier that works with all payment types, don’t include the [`paymentMethodType`](applepaymodifier/paymentmethodtype.md) attribute.

The following example shows a modifier that applies to the `credit` payment type that changes the total to $15, adds a $5 “Surcharge” line item, and adds a shipping method with an estimated delivery of 3 to 5 days:

```javascript
let shippingStart = new Date;
shippingStart.setDate(shippingStart.getDate() + 3);

let shippingEnd = new Date;
shippingEnd.setDate(shippingEnd.getDate() + 5);

let modifiers = [
    {
        supportedMethods: "https://apple.com/apple-pay",
        data: {
            paymentMethodType: "credit",
            total: {
                label: "Total",
                amount: "15.00",
            },
            additionalLineItems: [
                {
                    label: "Surcharge",
                    amount: "5.00",
                },
            ],
            additionalShippingMethods: [
                {
                    amount: "0.00",
                    dateComponentsRange: {
                        startDateComponents: {
                            year: shippingStart.getFullYear(),
                            months: shippingStart.getMonth() + 1,
                            days: shippingStart.getDate(),
                        },
                        endDateComponents: {
                            year: shippingEnd.getFullYear(),
                            months: shippingEnd.getMonth() + 1,
                            days: shippingEnd.getDate(),
                        },
                    },
                    detail: "Tickets sent to your address",
                    identifier: "delivery",
                    label: "Delivery",
                },
            ],
        },
    },
];
```

Applying the modifier overwrites the total in the payment request when the modifier also includes a total.

> ❗ **Important**:  The payment sheet displays data only. You’re responsible for supplying all values, including calculating new totals that result from using a modifier.

For more information about using the Apple Pay modifier, see [`Setting up the payment request API to accept Apple Pay`](setting-up-the-payment-request-api-to-accept-apple-pay.md).

##### Providing Multiple Modifiers

To provide an Apple Pay modifier that applies to all payment methods, include an [`ApplePayModifier`](applepaymodifier.md) with no [`paymentMethodType`](applepaymodifier/paymentmethodtype.md) specified. However, if this modifier appears first in an array of modifiers, the payment request always uses it, and ignores the subsequent Apple Pay modifiers.

If you provide multiple Apple Pay modifiers for the same [`paymentMethodType`](applepaymodifier/paymentmethodtype.md), such as multiple modifiers for a `"credit"` payment method type, Apple Pay uses only the first [`ApplePayModifier`](applepaymodifier.md) for that payment method. Apple Pay ignores the remaining modifiers with a `"credit"` payment method type.

##### Requesting Optional Payment Types

A typical payment request is for a one-time payment. To support different types of payment requests, include one of the following options in the [`ApplePayModifier`](applepaymodifier.md):

- The [`recurringPaymentRequest`](applepaymodifier/recurringpaymentrequest.md) property to request a recurring payment.
- The [`automaticReloadPaymentRequest`](applepaymodifier/automaticreloadpaymentrequest.md) property to set up automatic reload payments.
- The [`multiTokenContexts`](applepaymodifier/multitokencontexts.md) property to request multiple payment tokens to support multimerchant payments.

> **Note**:  You can set only one of these optional payment type properties in the [`ApplePayModifier`](applepaymodifier.md).

##### Requesting a Recurring Payment

Use the [`recurringPaymentRequest`](applepaymodifier/recurringpaymentrequest.md) property to set up a recurring payment request in the [`ApplePayModifier`](applepaymodifier.md). Recurring payments, such as subscriptions, can feature different payment intervals (for example, annually or monthly), and billing cycles (for example, regular or trial).

##### Requesting Automatic Reload Payments

Use the [`automaticReloadPaymentRequest`](applepaymodifier/automaticreloadpaymentrequest.md) property to set up an automatic reload payment in the [`ApplePayModifier`](applepaymodifier.md). You can set up automatic reload payments, such as store card top-ups, that feature a balance threshold and a reload amount. The card automatically reloads with the reload amount when the account drops below the balance threshold.

##### Requesting Multitoken or Multimerchant Payments

Use the [`multiTokenContexts`](applepaymodifier/multitokencontexts.md) property to set up payment data for multimerchant payments in the [`ApplePayModifier`](applepaymodifier.md). You can set up multitoken transactions to process and display payment requests with multiple merchants on one payment sheet, for example, a booking site where a user pays for a hotel, flight, and car rental from different merchants.

## Topics

### Payment method type
- [paymentMethodType](applepaymodifier/paymentmethodtype.md)
  The type of card the customer uses to complete the transaction.
- [ApplePayPaymentMethodType](applepaypaymentmethodtype.md)
  A string that represents the type of the payment method.
### Payment line items
- [total](applepaymodifier/total.md)
  A line item that represents the total payment.
- [additionalLineItems](applepaymodifier/additionallineitems.md)
  A set of line items that explain additional charges and discounts.
### Shipping methods
- [additionalShippingMethods](applepaymodifier/additionalshippingmethods.md)
  An array of shipping method dictionaries that describe the shipping methods that the payment request supports.
- [ApplePayShippingMethod](applepayshippingmethod.md)
  A dictionary that describes the shipping method for delivering physical goods.
### Updating recurring payments
- [recurringPaymentRequest](applepaymodifier/recurringpaymentrequest.md)
  A property that requests a recurring payment, typically a subscription.
- [ApplePayRecurringPaymentRequest](applepayrecurringpaymentrequest.md)
  A dictionary that represents a request to set up a recurring payment, typically a subscription.
### Updating automatic reload payments
- [automaticReloadPaymentRequest](applepaymodifier/automaticreloadpaymentrequest.md)
  A property that requests an automatic reload payment, such as a store card top-up.
- [ApplePayAutomaticReloadPaymentRequest](applepayautomaticreloadpaymentrequest.md)
  A dictionary that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
### Updating multitoken or multimerchant payments
- [multiTokenContexts](applepaymodifier/multitokencontexts.md)
  An array of payment token contexts that requests multiple payment tokens to support a multimerchant payment.
- [ApplePayPaymentTokenContext](applepaypaymenttokencontext.md)
  A dictionary that defines the context for a single payment token in a payment request for multimerchant payments.
### Updating deferred payments
- [deferredPaymentRequest](applepaymodifier/deferredpaymentrequest.md)
  A property that requests a recurring payment, such as a hotel booking or a pre-order.

## See Also

- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)
  Support payments using Apple Pay on your website.
- [ApplePayRequestBase](applepayrequestbase.md)
  A dictionary that defines basic payment and contact information that the Apple Pay payment request object uses for the W3C Payment Request API.
- [ApplePayRequest](applepayrequest.md)
  A dictionary that defines the Apple Pay payment request object to use for the W3C Payment Request API.
- [ApplePayPaymentCompleteDetails](applepaypaymentcompletedetails.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaymodifier)*