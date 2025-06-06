# openPaymentSetup

**Framework**: Apple Pay on the Web  
**Kind**: method

A method that displays the Set up Apple Pay button.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
static Promise <boolean> openPaymentSetup(
	DOMString merchantIdentifier
);
```

## Mentions

- [Apple Pay on the Web Version 2 Release Notes](apple-pay-on-the-web-version-2-release-notes.md)

#### Discussion

This method is available starting in iOS 10.1 and macOS 10.12.1. The code in `Listing 1` displays the Set up Apple Pay button if the method is available on a supported device and the user does not have Apple Pay set up yet.

Listing 1. Displaying either the Apple Pay button or the Set up Apple Pay button

```javascript
if (window.ApplePaySession) {
   var merchantIdentifier = 'example.com.store';
   var promise = ApplePaySession.canMakePaymentsWithActiveCard(merchantIdentifier);
   promise.then(function (canMakePayments) {
      if (canMakePayments) {
         // Display Apple Pay Buttons here…
      } else {
         // Check for the existence of the openPaymentSetup method.
         if (ApplePaySession.openPaymentSetup) {
            // Display the Set up Apple Pay Button here…             
            ApplePaySession.openPaymentSetup(merchantIdentifier)
               .then(function(success) {
		           if (success) {
			           // Open payment setup successful
		           } else {
			           // Open payment setup failed
		           }
               })
               .catch(function(e) {
		           // Open payment setup error handling
               });
         }
      }
  }); 
}
```

Use the HTML and CSS code in `Listing 2` to configure a Set up Apple Pay button for display.

Listing 2. Configuring a Set up Apple Pay button

```javascript
/* HTML */
<div class="apple-pay-set-up-button apple-pay-setup-button-white-with-line">
</div>
/* CSS */
.apple-pay-set-up-button {
    display: inline-block;
    -webkit-appearance: -apple-pay-button;
    -apple-pay-button-type: set-up;
}
.apple-pay-set-up-button-black {
    -apple-pay-button-style: black;
}
.apple-pay-set-up-button-white {
    -apple-pay-button-style: white;
}
.apple-pay-setup-button-white-with-line {
    -apple-pay-button-style: white-outline;
}
</style>
```

See [`Human Interface Guidelines > Apple Pay on the Web`](https://developer.apple.comhttps://developer.apple.com/apple-pay/web-human-interface-guidelines/) for information on how to use Apple Pay buttons.

## Parameters

- `merchantIdentifier`: The merchant ID created when the merchant enrolled in Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/openpaymentsetup)*