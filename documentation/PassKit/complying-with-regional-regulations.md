# Complying with regional regulations

**Framework**: PassKit (Apple Pay and Wallet)

Check regional regulations for possible requirements for your Apple Pay-based implementation.

#### Overview

Some regional regulations may require specific configurations in your Apple Pay implementation, such as including certain options in properties. Below is some guidance on configuring your implementation in current Apple Pay markets.

> **Note**:  This list may not be complete. Check with your payment service provider (PSP) or the appropriate authorities to ensure your implementation meets requirements.

- **United Kingdom and European Economic Area**: Transactions that take place in the United Kingdom and European Economic Area may be subject to The Payment Services Directive 2 (PSD2). Set the `countryCode` of the transaction to the region where it’s processed. Apple Pay uses the `countryCode` to generate data for the transaction that complies with this regulation. You’re also required to show a final amount on the payment sheet. For more information on PSD2, see [`Strong Customer Authentication Transactions in the European Economic Area`](https://developer.apple.comhttps://developer.apple.com/support/psd2/).
- **Saudi Arabia**: Saudi Arabia requires that all domestic debit transactions use the mada network. Merchants based in Saudi Arabia that support debit cards should add the [`mada`](pkpaymentnetwork/mada.md) payment network to their supported payment networks. If merchants don’t include `mada`, Apple Pay users may not be able to use certain Saudi-issued cards when the `countryCode` is `SA` (Saudi Arabia). Merchants using a PSP should confirm they support the mada network.
- **United Arab Emirates (UAE)**: The UAE requires that all domestic debit and prepaid transactions use the Jaywan network. Merchants based in UAE that support debit and prepaid cards should add the [`jaywan`](pkpaymentnetwork/jaywan.md) payment network to their supported payment networks. If merchants don’t include `jaywan`, Apple Pay users may not be able to use certain UAE-issued cards when the `countryCode` is `AE` (United Arab Emirates). Merchants using a PSP should confirm they support the Jaywan network.

## See Also

- [Setting up Apple Pay](setting-up-apple-pay.md)
  Fulfill the requirements to provide Apple Pay as a payment option on your website or in your app.
- [Offering Apple Pay in Your App](offering-apple-pay-in-your-app.md)
  Collect payments with iPhone and Apple Watch using Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/complying-with-regional-regulations)*