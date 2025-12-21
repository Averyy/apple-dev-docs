# Reporting tokens with transactions

**Framework**: External Purchase Server API

Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.

#### Overview

If your app uses [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase), you’re required to report all tokens and associated transactions according to the [`Commission, transaction reports, and payments`](https://developer.apple.comhttps://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu#commission-reports-and-payments) section of the article Using alternative payment options on the App Store in the European Union.

To send a report, call the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint for each token you receive.  A report has a request body, [`ExternalPurchaseReport`](externalpurchasereport.md), which consists of a unique report identifier, the token identifier, a status, and depending on the status, an array of line items that describe the transactions.

When a token has associated transactions, send a report with line items.  To correct a previous submission, see [`Reporting corrections`](reportcorrections.md). If the token didn’t result in any transactions, see [`Reporting unrecognized and transactionless tokens`](reportwithouttransactions.md) instead.

For each transaction, add one line item to the line items array in your report. Choose the line item type based on the transaction type:

- [`OneTimeBuyLineItem`](onetimebuylineitem.md) — for one-time charges
- [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md) - for transactions and events that involve subscriptions
- [`RefundLineItem`](refundlineitem.md) — for refunds

##### Create Line Items for One Time Charges

Use a [`OneTimeBuyLineItem`](onetimebuylineitem.md) object to specify a one-time charge in the `lineItems` array of the [`ExternalPurchaseReport`](externalpurchasereport.md).

The following example is an external purchase report with a single one-time charge transaction:

```json
{
    "requestIdentifier": "1cdc286e-7389-417c-b58f-7a7d196e5bbe",
    "externalPurchaseId": "2924c319-5205-4188-831a-1ca2c00326b4",
    "status": "LINE_ITEM",
    "lineItems": [{
        "lineItemId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
        "creationDate": 1706047472367,
        "eventType": "BUY",
        "productType": "ONE_TIME_BUY",
        "productIdentifier": "example.one-time-buy.product",
        "amountTaxInclusive": 10000,
        "amountTaxExclusive": 8000,
        "taxAmount": 2000,
        "netAmountTaxExclusive": 8000,
        "reportingCurrency": "EUR",
        "pricingCurrency": "EUR",
        "taxCountry": "ESP",
        "quantity": 6
    }]
}
```

##### Create Line Items for Subscription Events and Transactions

Use a [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md) object to specify a subscription-related transaction or event in the `lineItems` array of the [`ExternalPurchaseReport`](externalpurchasereport.md). The subscription events to report include subscription starts, renewals, changes to the subscription, and payments. Report subscription events even if they don’t include a payment. For more information, see [`subscriptionEvent`](subscriptionevent.md).

The following example is an external purchase report for an initial subscription purchase:

```json
{
    "requestIdentifier": "c4dcf1a5-afac-4e2c-83d7-280f9f2cb832",
    "externalPurchaseId": "59908800-c9d3-40c3-b638-8a9c5a535654",
    "status": "LINE_ITEM",
    "lineItems": [{
        "lineItemId": "cccccccc-cccc-cccc-cccc-cccccccccccc",
        "creationDate": 1706047488039,
        "eventType": "BUY",
        "productType": "SUBSCRIPTION",
        "productIdentifier": "example.subscription.monthly",
        "amountTaxInclusive": 10000,
        "amountTaxExclusive": 8000,
        "taxAmount": 2000,
        "netAmountTaxExclusive": 8000,
        "reportingCurrency": "EUR",
        "pricingCurrency": "EUR",
        "taxCountry": "ESP",
        "subscriptionEvent": "SUBSCRIPTION_START",
        "subscriptionStartDate": 1706047488039,
        "subscriptionEndDate": 1708639488039,
        "subscriptionDaysOfPaidService": 0,
        "quantity": 1
    }]
}
```

The following example is an external purchase report for a subscription renewal:

```json
{
    "requestIdentifier": "446fdfd8-2c06-4956-873c-8c449a9d61f5",
    "externalPurchaseId": "59908800-c9d3-40c3-b638-8a9c5a535654",
    "status": "LINE_ITEM",
    "lineItems": [{
        "lineItemId": "dddddddd-dddd-dddd-dddd-dddddddddddd",
        "creationDate": 1708639488039,
        "eventType": "BUY",
        "productType": "SUBSCRIPTION",
        "productIdentifier": "example.subscription.monthly",
        "amountTaxInclusive": 10000,
        "amountTaxExclusive": 8000,
        "taxAmount": 2000,
        "netAmountTaxExclusive": 8000,
        "reportingCurrency": "EUR",
        "pricingCurrency": "EUR",
        "taxCountry": "ESP",
        "subscriptionEvent": "RENEWAL",
        "subscriptionStartDate": 1708639488039,
        "subscriptionEndDate": 1711231488039,
        "subscriptionDaysOfPaidService": 30,
        "quantity": 1,
        "referenceLineItemId": "cccccccc-cccc-cccc-cccc-cccccccccccc"
    }]
}
```

##### Create Line Items for Refunds

Use a [`RefundLineItem`](refundlineitem.md) object to specify a refund transaction in the `lineItems` array of the [`ExternalPurchaseReport`](externalpurchasereport.md). Refunds include a `referenceLineItemId` that contains the `lineItemId` of a previously submitted transaction, to which the refund applies.

The following example is an external purchase report for a partial refund of the one-time charge shown in an earlier example:

```json
{
    "requestIdentifier": "b598cbea-c0a8-44cb-bb0e-abb12ed59cb9",
    "externalPurchaseId": "2924c319-5205-4188-831a-1ca2c00326b4",
    "status": "LINE_ITEM",
    "lineItems": [{
        "lineItemId": "bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb",
        "creationDate": 1706047491127,
        "eventType": "REFUND"
        "amountTaxInclusive": 2500,
        "amountTaxExclusive": 2000,
        "taxAmount": 500,
        "netAmountTaxExclusive": 6000,
        "reportingCurrency": "EUR",
        "pricingCurrency": "EUR",
        "taxCountry": "ESP",
        "referenceLineItemId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    }]
}
```

Use the `REFUND` value for [`eventType`](eventtype.md) to report chargebacks as well.

## See Also

- [Reporting corrections](reportcorrections.md)
  Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.
- [object OneTimeBuyLineItem](onetimebuylineitem.md)
  The line item that indicates a one-time charge transaction.
- [object RefundLineItem](refundlineitem.md)
  The line item that indicates a refund transaction.
- [object SubscriptionBuyLineItem](subscriptionbuylineitem.md)
  The line item that indicates a subscription-related event or transaction.
- [Line item fields](lineitems.md)
  Properties that describe a single transaction or correction in an external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithtransactions)*