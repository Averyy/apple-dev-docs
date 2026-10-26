# Payments

**Framework**: SiriKit  
**Role**: API Collection

Send payments between users or pay bills.

#### Overview

With the payments domain, users can pay bills or initiate monetary transfers between themselves and other individuals using Siri. Your Intents app extension facilitates bill payment from the user to any vendors (such as public utilities) that you previously configured in your app. For all payments, your Intents app extension works with your back-end services to initiate the transfers. The user then follows up on the progress of those transactions in your app.

![An image of a phone with Siri active, reporting progress at two different stages of a transaction. The image on the left shows Siri requesting confirmation to send an amount of money. The image on the right displays Siri’s confirmation that the money has been sent.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3743232@2x.png)

SiriKit automatically asks the user to unlock their device when processing any payment-related intents. You can provide a custom interface for payment-related intents using an Intents UI app extension.

## Topics

### Essentials
- [Handling Payment Requests with SiriKit](./handling-payment-requests-with-sirikit.md)
  Add an Intent Extension to your app to handle money transfer requests with Siri.
### Send a Payment
- [protocol INSendPaymentIntentHandling](https://developer.apple.com/documentation/intents/insendpaymentintenthandling)
  The handler interface for transferring money from the current user’s account to a different user’s account.
- [class INSendPaymentIntent](https://developer.apple.com/documentation/intents/insendpaymentintent)
  A request to transfer money from the current user’s account to a different user’s account.
- [class INSendPaymentIntentResponse](https://developer.apple.com/documentation/intents/insendpaymentintentresponse)
  Your app’s response to a send payment intent.
### Request a Payment
- [protocol INRequestPaymentIntentHandling](https://developer.apple.com/documentation/intents/inrequestpaymentintenthandling)
  The handler interface for delivering a request for payment from another user of your app.
- [class INRequestPaymentIntent](https://developer.apple.com/documentation/intents/inrequestpaymentintent)
  An intent for requesting money from another user’s account.
- [class INRequestPaymentIntentResponse](https://developer.apple.com/documentation/intents/inrequestpaymentintentresponse)
  Your app’s response to a request payment intent.
### Search for Accounts
- [protocol INSearchForAccountsIntentHandling](https://developer.apple.com/documentation/intents/insearchforaccountsintenthandling)
  The handler interface for searching for account information.
- [class INSearchForAccountsIntent](https://developer.apple.com/documentation/intents/insearchforaccountsintent)
  A user request for information about their accounts in your app.
- [class INSearchForAccountsIntentResponse](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponse)
  Your app’s response to a request to search for account information.
### Data Objects
- [enum INAccountType](https://developer.apple.com/documentation/intents/inaccounttype)
  Constants indicating the type of account involved in a financial transaction.
- [class INCurrencyAmount](https://developer.apple.com/documentation/intents/incurrencyamount)
  An amount of money to transfer during a financial transaction.
- [class INPaymentAccount](https://developer.apple.com/documentation/intents/inpaymentaccount)
  A user account that provides the funds when making a payment.
- [class INPaymentAmount](https://developer.apple.com/documentation/intents/inpaymentamount)
  The amount of money to apply to a bill payment.
- [class INPaymentMethod](https://developer.apple.com/documentation/intents/inpaymentmethod)
  Information about a form of payment supported by your app.
- [class INPaymentRecord](https://developer.apple.com/documentation/intents/inpaymentrecord)
  Detailed information about a financial transaction made between two users.
- [enum INPaymentStatus](https://developer.apple.com/documentation/intents/inpaymentstatus)
  Constants indicating the state of the financial transaction.
- [class INPerson](https://developer.apple.com/documentation/intents/inperson)
  Information about a person participating in a SiriKit interaction.
### Resolution Results
- [class INAccountTypeResolutionResult](https://developer.apple.com/documentation/intents/inaccounttyperesolutionresult)
  A resolution result for account types.
- [class INBalanceTypeResolutionResult](https://developer.apple.com/documentation/intents/inbalancetyperesolutionresult)
  A resolution result for balance types.
- [class INCurrencyAmountResolutionResult](https://developer.apple.com/documentation/intents/incurrencyamountresolutionresult)
  A resolution result for a currency amount associated with an intent.
- [class INPaymentAccountResolutionResult](https://developer.apple.com/documentation/intents/inpaymentaccountresolutionresult)
  A resolution result for the user account that provides the funds to pay a bill.
- [class INPaymentAmountResolutionResult](https://developer.apple.com/documentation/intents/inpaymentamountresolutionresult)
  A resolution result for the amount to pay for a bill.
- [class INPaymentMethodResolutionResult](https://developer.apple.com/documentation/intents/inpaymentmethodresolutionresult)
  Describes the result of resolving a payment method.
- [class INPaymentStatusResolutionResult](https://developer.apple.com/documentation/intents/inpaymentstatusresolutionresult)
  A resolution result for the payment status of a bill during a search.
- [class INRequestPaymentCurrencyAmountResolutionResult](https://developer.apple.com/documentation/intents/inrequestpaymentcurrencyamountresolutionresult)
  A resolution result for the currency amount associated with a payment request.
- [class INRequestPaymentPayerResolutionResult](https://developer.apple.com/documentation/intents/inrequestpaymentpayerresolutionresult)
  A resolution result for the person making the payment.
- [class INSendPaymentCurrencyAmountResolutionResult](https://developer.apple.com/documentation/intents/insendpaymentcurrencyamountresolutionresult)
  A resolution result for the currency amount to send to another user.
- [class INSendPaymentPayeeResolutionResult](https://developer.apple.com/documentation/intents/insendpaymentpayeeresolutionresult)
  A resolution result for the recipient of a payment.

## See Also

### Standard Intents
- [Car Commands](./car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Lists and Notes](./lists-and-notes.md)
  Create and manage notes and to-do list items.
- [Media](./media.md)
  Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.
- [Messaging](./messaging.md)
  Send messages and search the user’s received messages.
- [Restaurant Reservations](./restaurant-reservations.md)
  Create and manage restaurant reservations with help from the Maps app.
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/payments)*