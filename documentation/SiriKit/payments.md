# Payments

**Framework**: SiriKit  
**Role**: API Collection

Send payments between users or pay bills.

## Overview

With the payments domain, users can pay bills or initiate monetary transfers between themselves and other individuals using Siri. Your Intents app extension facilitates bill payment from the user to any vendors (such as public utilities) that you previously configured in your app. For all payments, your Intents app extension works with your back-end services to initiate the transfers. The user then follows up on the progress of those transactions in your app.

![An image of a phone with Siri active, reporting progress at two different stages of a transaction. The image on the left shows Siri requesting confirmation to send an amount of money. The image on the right displays Siri’s confirmation that the money has been sent.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3743232@2x.png)

SiriKit automatically asks the user to unlock their device when processing any payment-related intents. You can provide a custom interface for payment-related intents using an Intents UI app extension.

## Topics

### Essentials
- [Handling Payment Requests with SiriKit](./handling-payment-requests-with-sirikit.md)
  Add an Intent Extension to your app to handle money transfer requests with Siri.
### Send a Payment
- [protocol INSendPaymentIntentHandling](../Intents/insendpaymentintenthandling.md)
  The handler interface for transferring money from the current user’s account to a different user’s account.
- [class INSendPaymentIntent](../Intents/insendpaymentintent.md)
  A request to transfer money from the current user’s account to a different user’s account.
- [class INSendPaymentIntentResponse](../Intents/insendpaymentintentresponse.md)
  Your app’s response to a send payment intent.
### Request a Payment
- [protocol INRequestPaymentIntentHandling](../Intents/inrequestpaymentintenthandling.md)
  The handler interface for delivering a request for payment from another user of your app.
- [class INRequestPaymentIntent](../Intents/inrequestpaymentintent.md)
  An intent for requesting money from another user’s account.
- [class INRequestPaymentIntentResponse](../Intents/inrequestpaymentintentresponse.md)
  Your app’s response to a request payment intent.
### Search for Accounts
- [protocol INSearchForAccountsIntentHandling](../Intents/insearchforaccountsintenthandling.md)
  The handler interface for searching for account information.
- [class INSearchForAccountsIntent](../Intents/insearchforaccountsintent.md)
  A user request for information about their accounts in your app.
- [class INSearchForAccountsIntentResponse](../Intents/insearchforaccountsintentresponse.md)
  Your app’s response to a request to search for account information.
### Data Objects
- [enum INAccountType](../Intents/inaccounttype.md)
  Constants indicating the type of account involved in a financial transaction.
- [class INCurrencyAmount](../Intents/incurrencyamount.md)
  An amount of money to transfer during a financial transaction.
- [class INPaymentAccount](../Intents/inpaymentaccount.md)
  A user account that provides the funds when making a payment.
- [class INPaymentAmount](../Intents/inpaymentamount.md)
  The amount of money to apply to a bill payment.
- [class INPaymentMethod](../Intents/inpaymentmethod.md)
  Information about a form of payment supported by your app.
- [class INPaymentRecord](../Intents/inpaymentrecord.md)
  Detailed information about a financial transaction made between two users.
- [enum INPaymentStatus](../Intents/inpaymentstatus.md)
  Constants indicating the state of the financial transaction.
- [class INPerson](../Intents/inperson.md)
  Information about a person participating in a SiriKit interaction.
### Resolution Results
- [class INAccountTypeResolutionResult](../Intents/inaccounttyperesolutionresult.md)
  A resolution result for account types.
- [class INBalanceTypeResolutionResult](../Intents/inbalancetyperesolutionresult.md)
  A resolution result for balance types.
- [class INCurrencyAmountResolutionResult](../Intents/incurrencyamountresolutionresult.md)
  A resolution result for a currency amount associated with an intent.
- [class INPaymentAccountResolutionResult](../Intents/inpaymentaccountresolutionresult.md)
  A resolution result for the user account that provides the funds to pay a bill.
- [class INPaymentAmountResolutionResult](../Intents/inpaymentamountresolutionresult.md)
  A resolution result for the amount to pay for a bill.
- [class INPaymentMethodResolutionResult](../Intents/inpaymentmethodresolutionresult.md)
  Describes the result of resolving a payment method.
- [class INPaymentStatusResolutionResult](../Intents/inpaymentstatusresolutionresult.md)
  A resolution result for the payment status of a bill during a search.
- [class INRequestPaymentCurrencyAmountResolutionResult](../Intents/inrequestpaymentcurrencyamountresolutionresult.md)
  A resolution result for the currency amount associated with a payment request.
- [class INRequestPaymentPayerResolutionResult](../Intents/inrequestpaymentpayerresolutionresult.md)
  A resolution result for the person making the payment.
- [class INSendPaymentCurrencyAmountResolutionResult](../Intents/insendpaymentcurrencyamountresolutionresult.md)
  A resolution result for the currency amount to send to another user.
- [class INSendPaymentPayeeResolutionResult](../Intents/insendpaymentpayeeresolutionresult.md)
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