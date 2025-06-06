# Setting up the payment request API to accept Apple Pay

**Framework**: Apple Pay on the Web

Support payments using Apple Pay on your website.

#### Overview

Throughout the [`W3C Payment Request API specification`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/), properties and attributes with the type `object` contain specific data related to payment methods. When using Apple Pay, keep in mind that these properties and attributes with the type `object` have a concrete type.

To indicate that data is specific to Apple Pay, set the [`supportedMethods`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#dom-paymentmethoddata-supportedmethods) property of the W3C [`PaymentMethodData`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentmethoddata-dictionary) dictionary and W3C [`PaymentDetailsModifier`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentdetailsmodifier-dictionary) dictionary to the Apple Pay URL `https://apple.com/apple-pay`.

Set up the payment request by setting the [`data`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#dom-paymentmethoddata-data) property of the W3C [`PaymentMethodData`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentmethoddata-dictionary) dictionary to an [`ApplePayRequest`](applepayrequest.md) dictionary. The following is an example of an [`ApplePayRequest`](applepayrequest.md) dictionary that requires Apple Pay Version 12:

```javascript
let applePayPaymentMethodData = {
    supportedMethods: "https://apple.com/apple-pay",
    data: {
        version: 12,
        // Add additional ApplePayRequest attributes here.
    },
};
```

Customize the payment request by setting the [`data`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#dom-paymentdetailsmodifier-data) property of the W3C [`PaymentDetailsModifier`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentdetailsmodifier-dictionary) dictionary to an [`ApplePayModifier`](applepaymodifier.md) dictionary. The following is an example of an [`ApplePayModifier`](applepaymodifier.md) dictionary that only applies to credit cards:

```javascript
let applePayPaymentDetailsModifier = {
    supportedMethods: "https://apple.com/apple-pay",
    data: {
        paymentMethodType: "credit",
        // Add additional ApplePayModifier attributes here.
    },
};
```

Handle changes made by the user to features specific to Apple Pay by looking at the [`methodDetails`](paymentmethodchangeevent/methoddetails.md) attribute of the W3C [`PaymentMethodChangeEvent`](paymentmethodchangeevent.md):

- If the user changes the payment method type, the [`methodDetails`](paymentmethodchangeevent/methoddetails.md) attribute is an [`ApplePayPaymentMethod`](applepaypaymentmethod.md) dictionary.
- If the user changes the coupon code, the [`methodDetails`](paymentmethodchangeevent/methoddetails.md) attribute is an [`ApplePayCouponCodeDetails`](applepaycouponcodedetails.md) dictionary.

The following is an example of how to differentiate these different scenarios when handling a W3C [`PaymentMethodChangeEvent`](paymentmethodchangeevent.md):

```javascript
paymentRequest.addEventListener("paymentmethodchange", function(event) {
    if (event.methodName === "https://apple.com/apple-pay") {
        if (event.methodDetails.couponCode) {
            let applePayCouponCodeDetails = event.methodDetails;
            // Handle coupon code updates here.
            return;
        }

        let applePayPaymentMethodDetails = event.methodDetails;
        if (applePayPaymentMethodDetails.type === "credit") {
            // Handle credit payment method type changes here.
        } else {
            // Handle other payment method type changes here.
        }
    }
});
```

Explain issues by creating custom error messages using an array of [`ApplePayError`](applepayerror.md) objects:

- If the user makes any problematic changes, set the [`paymentMethodErrors`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#dom-paymentdetailsupdate-paymentmethoderrors) property of the W3C [`PaymentDetailsUpdate`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentdetailsupdate-dictionary) dictionary.
- If a problem occurs during authorization, set the [`paymentMethod`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#dom-paymentvalidationerrors-paymentmethod) property of the W3C [`PaymentValidationErrors`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#dom-paymentvalidationerrors) dictionary.

The following is an example of how to show custom error messages if the user inputs an invalid coupon code or shipping postal code:

```javascript
paymentRequest.addEventListener("shippingaddresschange", function(event) {
    if (event.methodName === "https://apple.com/apple-pay") {
        if (event.methodDetails.couponCode) {
            let applePayCouponCodeDetails = event.methodDetails;
            if (!isValidCouponCode(applePayCouponCodeDetails.couponCode) {
                event.updateWith({
                    paymentMethodErrors: [
                        new ApplePayError("couponCodeInvalid", undefined, "Coupon code is invalid"),
                    ],
                });
                return;
            }

            // Handle valid coupon code updates here.
            return;
        }

        let applePayPaymentMethodDetails = event.methodDetails;
        if (applePayPaymentMethodDetails.type === "credit") {
            // Handle credit payment method type changes here.
        } else {
            // Handle other payment method type changes here.
        }
    }
});

paymentRequest.show().then(function(paymentResponse) {
    if (paymentResponse.methodName === "https://apple.com/apple-pay") {
        if (!hasValidShippingZIPCode(paymentResponse)) {
            paymentResponse.retry({
                paymentMethod: [
                    new ApplePayError("shippingContactInvalid", "postalCode", "ZIP Code is invalid"),
                ],
            });
            return;
        }

        // Handle authorization with valid details here.
    }
});

```

Get the payment information after the user authorizes the payment request by looking at the [`details`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#dom-paymentresponse-details) attribute of the W3C [`PaymentResponse`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentresponse-interface), which is an [`ApplePayPayment`](applepaypayment.md) dictionary. The following example accesses the [`postalCode`](applepaypaymentcontact/postalcode.md) after authorization:

```javascript
function hasValidShippingZIPCode(paymentResponse) {
    if (paymentResponse.methodName === "https://apple.com/apple-pay") {
        let applePayPayment = paymentResponse.details;
        let shippingZIPCode = applePayPayment.shippingContact.postalCode;
        // Validate shipping ZIP code here.
    }
}
```

## See Also

- [ApplePayRequestBase](applepayrequestbase.md)
  A dictionary that defines basic payment and contact information that the Apple Pay payment request object uses for the W3C Payment Request API.
- [ApplePayRequest](applepayrequest.md)
  A dictionary that defines the Apple Pay payment request object to use for the W3C Payment Request API.
- [ApplePayModifier](applepaymodifier.md)
  A dictionary that defines the Apple Pay modifiers for a payment type in the W3C Payment Request API.
- [ApplePayPaymentCompleteDetails](applepaypaymentcompletedetails.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/setting-up-the-payment-request-api-to-accept-apple-pay)*